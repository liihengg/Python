# def foo():
#     global a
#     a = 200
#     print(a)
# 
# 
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)
# 

def foo():
    a = 200
    print(a)

    def bar():
        nonlocal a
        a = 100
        print(a)

    bar()
    print(a)


if __name__ == '__main__':
    foo()
