from threading import Thread
import time
import requests
import os
from lxml import html
from enum import Enum

fileEncoding = 'utf-8'

resourcePth = '../Resource'
urlContentPath = resourcePth + '/urlContent.html'
textureUrl = 'https://meirentu.cc/pic/984846992922.html'
globalInfoTextPath = resourcePth + '/Texture/GlobalText.text'


class UrlState(Enum):
    NotStarted = 1
    Downloading = 2
    Done = 3
    Failed = 4


class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        fileName = "1"
        resp = requests.get(
            self._url,
            headers={
                'Referer': 'https://meirentu.cc/pic/984846992922-14.html'}
        )
        if resp.status_code == 200:
            with open('../Resource/Texture/3.jpg', 'wb') as f:
                f.write(resp.content)
        else:
            print(resp.status_code)
            print(resp.text)


def CheckUrlState(url):
    try:
        with open(globalInfoTextPath, 'a+', fileEncoding) as f:
            globalInfo = f.read()
            hasUrl: bool = False
            for k, v in globalInfo:
                if k == url:
                    print(k)
    except FileNotFoundError:
        print()


def CreateInfoFile(htmlTree):
    title = htmlTree.xpath('body//div[@class="item_title"]/h1/text()')
    print(title[0])
    info = htmlTree.xpath('body//article/p/text()')
    for a in info:
        print(a)


def main():
    CheckUrlState('12345678')
    # if os.path.exists('../Resource/Texture/1'):
    #     print('文件已存在')
    # else:
    #     os.mkdir('../Resource/Texture/1')

    # resp = requests.get(textureUrl)
    # resp.text.
    # with open(urlContentPath, 'w', encoding=fileEncoding) as f:
    #     f.write(resp.text)
    #     urlContent = resp.text

    # DownloadHandler('https://cdn2.mmdb.cc/file/20230610/984846992922/04080472.jpg').start()
    # with open(urlContentPath, 'r', encoding=fileEncoding) as f:
    # with open('../Resource/testHtml.html', 'r', encoding=fileEncoding) as f:

    # text = f.read()
    # tree = html.fromstring(text)
    # CreateInfoFile(tree)

    # article = tree.xpath('head/title[1]/text()')
    # title = tree.xpath('body/div[2]/div[1]/div[1]/div[1]')
    # article = tree.xpath('head/meta[1]')
    # for a in article:
    #    print(a.attrib)


if __name__ == '__main__':
    main()
