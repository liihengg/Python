from threading import Thread
import requests
import json
import os
from lxml import html
import MetaFileUtils as meta_file_utils

fileEncoding = 'utf-8'

resourcePath = '../Resource'
textureFilePath = resourcePath + '/Texture'

downloadMetaPath = resourcePath + '/DownloadMeta.json'
downloadIndexFilePath = resourcePath + '/index.txt'

rootUrl = 'https://meirentu.cc'

NotStarted: int = 1
Downloading: int = 2
Done: int = 3
Failed: int = 4

CountByUrl = "CountByUrl"
CountByDownload = "CountByDownload"


class DownloadHandler(Thread):
    def __init__(self, url, headers, callback):
        super().__init__()
        self._url = url
        self._headers = headers
        self._callback = callback

    def run(self):
        resp = requests.get(
            self._url,
            headers=self._headers,
        )
        self._callback(resp, self._url)


def CheckUrlState(url):
    # 检查这个组是否下载过

    with open(downloadMetaPath, 'r', encoding=fileEncoding) as f:
        jsonData = json.load(f)
        for k, v in jsonData.items():
            if k == url:
                return v

    with open(downloadMetaPath, 'w', encoding=fileEncoding) as f:
        jsonData[url] = NotStarted
        json.dump(jsonData, f)
        return NotStarted


def UpdateUrlState(url, state):
    with open(downloadMetaPath, 'r', encoding=fileEncoding) as f:
        jsonData = json.load(f)
        for k, v in jsonData.items():
            if k == url:
                jsonData[k] = state

    with open(downloadMetaPath, 'w', encoding=fileEncoding) as f:
        json.dump(jsonData, f)


def DownloadTexture(url, headers, savePath):
    # 下载具体的图片

    def callback(resp, request_url):
        if resp.status_code == 200:
            with open(savePath, 'wb') as f:
                f.write(resp.content)

    DownloadHandler(url, headers, callback).start()


def CreateInfoFile(htmlTree):
    # 写入简介

    dicPath = ''
    # 拿到title
    title = htmlTree.xpath('body//div[@class="item_title"]/h1/text()')
    # 判断title是否合法 todo 临时方案
    if len(title) <= 0:
        return dicPath

    dicPath = textureFilePath + '/' + title[0]
    # 判断是否存在路径，不存在创建
    if not os.path.exists(dicPath):
        os.mkdir(dicPath)

    infos = htmlTree.xpath('body//article/p/text()')
    infoFilePath = dicPath + '/info.txt'
    with open(infoFilePath, 'w', encoding=fileEncoding) as f:
        content: str = ''
        for info in infos:
            content += info + "\n"
        f.write(content)
    return dicPath


def DownloadGroupTexture(url):
    # 下载一组图片

    # 先检查当前url的状态
    urlState = CheckUrlState(url)
    match urlState:
        case 1:  # 如果是 NotStarted 状态，更新一下
            UpdateUrlState(url, Downloading)
        case 2:
            pass
        case _:  # 其他状态，不继续处理
            return

    # 开始处理url
    resp = requests.get(url)
    if resp.status_code != 200:
        return

    rootHtmlTree = html.fromstring(resp.text)
    # 先创建 url 信息文件
    dicPath = CreateInfoFile(rootHtmlTree)
    if len(dicPath) <= 0:
        UpdateUrlState(url, Failed)
    # find all page url
    all_part_url = rootHtmlTree.xpath('body//div[@class="main_left"]//div[@class="content"][2]'
                                      '//div[@class="page"]//a/@href')
    for i in range(len(all_part_url) - 1):
        full_part_url = rootUrl + all_part_url[i]
        resp = requests.get(full_part_url)
        if resp.status_code != 200:
            return
        cur_part_html_tree = html.fromstring(resp.text)
        # get current page texture url
        cur_part_html_tree_urls = cur_part_html_tree.xpath('body//div[@class="main_left"]//div[@class="content"][1]'
                                                           '//div/img/@src')
        print(full_part_url)
        for current_texture_url in cur_part_html_tree_urls:
            start_index = current_texture_url.rfind('/')
            file_name = current_texture_url[start_index + 1:]
            headers = {'Referer': full_part_url}
            DownloadTexture(current_texture_url, headers, dicPath + '/' + file_name)

    UpdateUrlState(url, Done)


def DownloadPage(start_index):
    cur_index = start_index
    while True:
        page_url = f'https://meirentu.cc/index/{cur_index}.html'
        resp = requests.get(page_url)
        if resp.status_code != 200:
            continue

        page_html_tree = html.fromstring(resp.text)
        all_group_url = page_html_tree.xpath('body//ul[@class="update_area_lists cl"]//li/a/@href')
        for group_url in all_group_url:
            DownloadGroupTexture(rootUrl + group_url)
        cur_index = cur_index + 1
        with open(downloadIndexFilePath, 'w', encoding=fileEncoding) as f:
            f.write(str(cur_index))


def main():
    meta_file_utils.check_meta_file()
    start_index = meta_file_utils.get_start_index()
    if start_index == -1:
        start_index = 1

    DownloadPage(start_index)


if __name__ == '__main__':
    main()
