"""Создайте класс Архив, который хранит пару свойств. Например, число и строку.
 - При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
 - list-архивы также являются свойствами экземпляра
"""
"""Доработаем класс Архив из задачи 2. 
 - Добавьте методы представления экземпляра для программиста и для пользователя.
"""


class Archive:
    """Сохраняем данные каждого экземпляра класса в списки numbers values"""
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """Переопределили метод new для сохранения аргументов в списки"""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        """Определили метод инициализации экземпляра класса"""
        self.number = number
        self.value = value

    def __repr__(self):
        """Переопределеный дандер метод предствления объекта полезный для отладки"""
        return f'Archive({self.number}, "{self.value}")'

    def __str__(self):
        """Переопределенный дандер метод строчного предствления объекта"""
        return f'Номер: {self.number}, Значение: "{self.value}"'


if __name__ == '__main__':
    a1 = Archive(1, "Один")
    # a2 = Archive(2, "Два")
    # print(f'{a1.numbers} {a1.values}')
    # print(f'{a2.numbers} {a2.values}')
    # a_3 = Archive(3, "Три")
    # print(f'{a_3.numbers} {a_3.values}')
    # help(a1)
    print(a1.__repr__())
    print(f'{a1 = }')
    print(a1)
    help(Archive)
