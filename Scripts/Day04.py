# sum = 0
# for x in range(100, 0, -2):
#     sum += x
# print(sum)
# 
# import random
# 
# answer = random.randint(1, 100)
# counter = 0
# isContinue = True
# while isContinue:
#     counter += 1
#     number = int(input('please input a number: '))
#     if number < answer:
#         print('小了')
#     elif number > answer:
#         print('大了')
#     else:
#         print('对了')
#         isContinue = False
# print('一共猜了%d次' % counter)

for x in range(1, 10):
    for y in range(1, x + 1):
        print('%d x %d = %d' % (y, x, x * y), end='\t')
    print()
