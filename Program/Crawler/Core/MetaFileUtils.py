import ConstFields as const
import json
import os


def check_meta_file():
    if not os.path.exists(const.resource_path):
        os.mkdir(const.resource_path)

    if not os.path.exists(const.texture_file_path):
        os.mkdir(const.texture_file_path)

    if not os.path.exists(const.download_meta_path):
        with open(const.download_meta_path, 'w', encoding=const.UTF_8) as f:
            # Creating a meta file for the first time: Write json template
            default_dic = {'url': {const.count_by_url: 1, const.count_by_download: 1}}
            json.dump(default_dic, f)

    if not os.path.exists(const.download_index_file_path):
        with open(const.download_index_file_path, 'w', encoding=const.UTF_8) as f:
            f.write(str(1))


def get_start_index():
    try:
        with open(const.download_index_file_path, 'r', encoding=const.UTF_8) as f:
            return int(f.read())
    except:
        return -1
