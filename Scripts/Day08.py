class Student(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def study(self, course_name):
        print(f'{self.name} is learning {course_name}')


def main():
    stu1 = Student('a', 20)
    stu1.study('Chinese')
    stu2 = Student('b', 40)
    stu2.study('English')


if __name__ == '__main__':
    main()
