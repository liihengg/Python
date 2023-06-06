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
# class Student(Person):
#     # __slots__ = ('__name', '__age', '__aaa')
# 
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self.__grade = grade
# 
#     @property
#     def grade(self):
#         return self.__grade
# 
#     @grade.setter
#     def grade(self, grade):
#         self.__grade = grade
# 
# 
# class Teacher(Person):
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self.__title = title
# 
#     @property
#     def title(self):
#         return self.__title
# 
#     @title.setter
#     def title(self, title):
#         self.__title = title
# 
# 
# def main():
#     p = Person('name', 12)
#     print('--------------')
#     print(p.name)
#     print(p.age)
#     p.age = 13
#     print(p.age)
#     p._Person__gender = 1
#     print(p.gender)
# 
#     print('--------------')
#     stu = Student('student', 13, '初二')
#     stu._Person__gender = 1
#     print(stu.gender)


# 
# class Triangle(object):
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
# 
#     @staticmethod
#     def IsValid(a, b, c):
#         return a + b > c and b + c > a and a + c > b
# 
#     def perimeter(self):
#         return self.__a + self.__b + self.__c
# 
# 
# def main():
#     a, b, c = 3, 4, 5
#     if Triangle.IsValid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())

from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self.__nickname = nickname

    @property
    def nickname(self):
        return self.__nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    def make_voice(self):
        print(f'{self.nickname} 是 狗')


class Cat(Pet):
    def make_voice(self):
        print(f'{self.nickname} 是 猫')


def main():
    pets = [Dog('狗1'), Cat('猫1')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
