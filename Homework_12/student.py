import csv

class Family:
    def __init__(self, family: str = None):
        self.family = family

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value):

        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if self.family is not value.istitle():
            raise ValueError(f'Значение {value} должно быть с большой буквы')

class Subjects:
    def __init__(self, subject: str = None):
        self.subject = subject

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def subject(self):
        sub_list = []
        with open('subjects.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                sub_list.append(row)
    def validate(self, value):

        if not value in self.sub_list:
            raise TypeError(f'Предмет {value} не входит в утвержденный перечень')

class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value):

        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно{self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')

class Student:
    name = Family
    subject = Subjects
    test = Range(1, 100)
    grade = Range(2, 5)

    def __init__(self, name, subject, test, grade):
        self.name = name
        self.subject = subject
        self.test = test
        self.grade = grade


    def __repr__(self):
        return f'Student(name={self.name}, предмет={self.subject} тест={self.test}  оценка={self.grade} )'


if __name__ =='__main__':
    std_one = Student('Архимед', 'биология', 99, 4)
    print(f'{std_one   = }')
    print(Student.subject())

