"""Создайте класс Моя Строка, где:
 - будут доступны все возможности str
 - дополнительно хранятся имя автора строки и время создания (time.time)
"""
from time import time


class MyStr(str):
    """ Расширяемый класс str. """

    def __new__(cls, value, name: str):
        """Расширяем метод new параметрами name и value"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time()
        return instance

    def __str__(self):
        """Переопределенный дандер метод строчного предствления объекта"""
        return f'Имя автора: {self.name}, Время создания: "{self.created_at}"'


if __name__ == '__main__':
    mystr = MyStr('Строка', 'Устинова')
    print(mystr.name)
    print(mystr.created_at)
    print(mystr)
    print(mystr.upper())
    help(MyStr)
