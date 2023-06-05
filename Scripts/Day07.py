# s1 = 'hello, world!'
# s2 = "hello, world!"
# # 以三个双引号或单引号开头的字符串可以折行
# s3 = """
# world!
# """
# print(s1, s2, s3, end='')
# import sys

# s1 = '\t a \t'
# s2 = r'\t a \t'
# print(s1)
# print(s2)

# s1 = '123' * 3
# print(s1)
# s2 = ' 4'
# s1 += s2
# print(s1)
# print('4' not in s1)
# print('a' in s1)

# s3 = '  1234567a '
# print(s3[2])
# print(s3[2:5])
# print(s3[2:])
# print(s3[2::3])
# print(s3[::3])
# print(s3[::-1])
# print(s3[-3::-1])
# print(len(s3))
# print(s3.capitalize())
# print(s3.find('7'))
# print(s3.find('9'))
# print(s3.index('9'))
# print(s3.center(20, '*'))
# print(s3.rjust(20, '*'))
# print(s3.isdigit())
# print(s3.isalpha())
# print(s3.isalnum())
# print(s3)
# print(s3.strip())
# a = 1
# b = 2
# print(f'{a} + {b} = {a + b}')

# list1 = [1, 3, 5, 7, 100]
# print(list1)
# list2 = ['hello'] * 3
# print(list2)
# print(len(list1))
# print(list1[0])
# print(list1[3])
# print(list1[-1])
# print(list1[-4])
# print('------------------')

# for i in range(len(list1)):
#     print(list1[i])
# print('------------------')
# for elem in list1:
#     print(elem)
# print('------------------')
# for k, v in enumerate(list1):
#     print(k, v)

# list1 = [1, 3, 5, 7, 100, 1]
# # list1.append(200)
# list1.insert(1, 400)
# list2 = list1
# # list1 += list2
# print(list1)
# print(list2)
# if 1 in list1:
#     list1.remove(1)
# while 1 in list1:
#     list1.remove(1)
# print(list1)
# list1.pop(1)
# print(list1)
# list1.pop(-1)
# print(list1)
# list1.clear()
# print(list1)
# print(list2)
# list1 = ['grape', 'apple', 'strawberry', 'wax berry', 'pita', 'pear', 'mango']
# list2 = sorted(list1)
# print(list2)
# list3 = sorted(list1, reverse=True)
# print(list3)
# list4 = sorted(list1, key=len)
# print(list4)
# list1.sort(reverse=True)
# print(list1)
# list1.sort(key=len, reverse=True)
# print(list1)

# f1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# f2 = [x for x in range(21)]
# f3 = (x for x in range(21))
# print(f1)
# print(f2)

# print('[', end='')
# for f in f3:
#     print(f' {f},', end='')
# print(']')

# print(sys.getsizeof(f1))
# print(sys.getsizeof(f2))
# print(sys.getsizeof(f3))

# f = [x + y for x in 'abcde' for y in '123456']
# print(f)

# f2 = (x for x in range(10))
# print(f2[0])

# t = ("1", 1)
# print(t)
# list1 = list(t)
# print(list1)
# t2 = tuple(list1)
# print(t2)

# set1 = {1, 2, 3, 4, 4, 5, 2}
# print(set1)
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 4, 4, 5, 2))
# print(set2, set3)
# set4 = {num for num in range(1, 100) if num % 3 == 0}
# print(set4)

# set2 = set(range(1, 10))
# set2.add(200)
# print(set2)
# set2.discard(100)
# print(set2)
# set2.update([10, 50, 30])
# print(set2)
# set2.remove(10)
# print(set2)
# print(set2.pop())
# print(set2)

# set1 = set(range(1, 6))
# set2 = set(range(5, 10))
# print(set1, set2)
# print(set1 & set2)
# print(set1 | set2)
# print(set1 - set2)
# print(set2 - set1)
# print(set1 ^ set2)
# print(set2 ^ set1)
# print('----------')
# set3 = {4}
# print(set1 > set3)
# print(set2 > set3)
# # print(set3 in set2)

# dict1 = {'key1': 1, 'key2': 2}
# print(dict1)
# dict2 = dict(one=1, key2=2)
# print(dict2)
# dict3 = dict(zip(['a', 'b', 'c'], '123'))
# print(dict3)
# dict4 = {num: num ** 2 for num in range(9)}
# print(dict4)
# print(dict1['key1'])
# # print(dict3('a')) # error
# # print(dict4(3)) # error
# dict1.update(a=1)
# print(dict1)
# dict1.update(a=2)
# print(dict1)
# print(dict1.get('key3', 10))
# dict1.popitem()
# print(dict1)
# item = dict1.pop('key1', 10)
# print(item)
# print(dict1)

# import os
# import time
# 
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]
# 
# 
# if __name__ == '__main__':
#     main()

import random


# def main(code_len=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     code = ''
#     last_pos = len(all_chars) - 1
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code

def main(filename, has_dot=False):
    pos = filename.find('.')
    if pos != -1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    a = main("1234.xt", True)
    print(a)
