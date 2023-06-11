import time

# def main():
# try:
#     with open('../Resource/1.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
# except FileNotFoundError:
#     print('无法打开指定文件')
# except LookupError:
#     print('指定了未知的编码')
# except UnicodeDecodeError:
#     print('读取文件时解码错误')

# f = None
# try:
#     f = open('1.txt', 'r', encoding='utf-8')
#     print(f.read())
# except FileNotFoundError:
#     print('无法打开指定文件')
# except LookupError:
#     print('指定了未知的编码')
# except UnicodeDecodeError:
#     print('读取文件时解码错误')
# finally:
#     if f:
#         f.close()

# filePath = '../Resource/1.txt'

# with open('../Resource/1.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
# 
# with open('../Resource/1.txt', mode='r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')
#         time.sleep(0.5)
# print()
# 
# with open('../Resource/1.txt', mode='r', encoding='utf-8') as f:
#     lines = f.readlines()
# print(lines)

# f = open(filePath, 'a', encoding='utf-8')
# f.writelines('6666')

# with open(filePath, 'rb') as f1:
#     data = f1.read()
# with open('2', 'wb') as f2:
#     f2.write(data)

# import json
# 
# 
# def main():
#     mydict = {
#         'name': 'aaa',
#         'age': 38,
#         'friends': ['bbb', 'ccc'],
#         'cars': [
#             {'type': 'car1'},
#             {'type': 'car2'},
#             {'type': 'car3'},
#         ]
#     }
#     try:
#         with open('../Resource/myJson.json', 'w', encoding='utf-8') as f:
#             json.dump(mydict, f)
#     except IOError as e:
#         print(e)
#     

import requests


def main():
    state = 1
    for index in range(1,4):
        print(index)
    # resp = requests.get('https://www.baidu.com')
    # print(resp.text)


if __name__ == '__main__':
    main()
