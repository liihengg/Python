# class Person(object):
#     __slots__ = ('__name', '__age', '__gender')
# 
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
# 
#     @property
#     def name(self):
#         return self.__name
# 
#     @property
#     def age(self):
#         return self.__age
# 
#     @age.setter
#     def age(self, age):
#         self.__age = age
# 
#     @property
#     def gender(self):
#         return self.__gender
# 
# 
# def main():
#     p = Person('name', 12)
#     print(p.name)
#     print(p.age)
#     p.age = 13
#     print(p.age)
#     p._Person__gender = 1
#     print(p.gender)


class Triangle(object):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @staticmethod
    def IsValid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self.__a + self.__b + self.__c


def main():
    a, b, c = 3, 4, 5
    if Triangle.IsValid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())


if __name__ == '__main__':
    main()
