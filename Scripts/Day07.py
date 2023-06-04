# s1 = 'hello, world!'
# s2 = "hello, world!"
# # 以三个双引号或单引号开头的字符串可以折行
# s3 = """
# world!
# """
# print(s1, s2, s3, end='')
import sys

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
# 
# print('[', end='')
# for f in f3:
#     print(f' {f},', end='')
# print(']')
# 
# print(sys.getsizeof(f1))
# print(sys.getsizeof(f2))
# print(sys.getsizeof(f3))

# f = [x + y for x in 'abcde' for y in '123456']
# print(f)

# f2 = (x for x in range(10))
# print(f2[0])

t = ("1", 1)
print(t)
list1 = list(t)
print(list1)
t2 = tuple(list1)
print(t2)
