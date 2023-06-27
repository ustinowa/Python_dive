"""Дорабатываем класс прямоугольник из прошлого семинара.
📌Добавьте возможность сложения и вычитания.
📌При этом должен создаваться новый экземпляр прямоугольника.
📌Складываем и вычитаем периметры, а не длинну и ширину.
📌При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    """Класс прямоугольник, с методами расчета периметра и площади фигуры."""

    def __init__(self, side1: int, side2: int = None):
        """Метод инициализации прямоугольника со сторонами a и b."""
        self.side1 = side1
        self.side2 = side2 if side2 is not None else side1

    def area(self) -> int:
        """Метод расчета площади прямоугольника"""
        return self.side2 * self.side1

    def perimetr(self) -> int:
        """Метод расчета периметра прямоугольника"""
        return 2 * (self.side1 + self.side2)

    def __add__(self, other):
        """Переопределенный дандер метод сложения двух прямоугольников"""
        new_perimetr = self.perimetr() + other.perimetr()
        new_side1 = self.side1
        new_side2 = new_perimetr / 2 - new_side1
        return Rectangle(new_side1, new_side2)

    def __sub__(self, other):
        """Переопределенный дандер метод вычетания двух прямоугольников"""
        new_perimetr = abs(self.perimetr() - other.perimetr())
        new_side1 = min([self.side1, self.side2, other.side1, other.side2])
        new_side2 = new_perimetr / 2 - new_side1
        return Rectangle(new_side1, new_side2)

    def __str__(self):
        """Переопределенный дандер метод строчного выведения экземпляра класса"""
        return f'Прямоугольник {self.side1} x {self.side2}'


if __name__ == '__main__':
    rect1 = Rectangle(10, 20)
    rect2 = Rectangle(10)
    # print(f'{rect1.perimetr()=}, {rect1.area()=}')
    # print(f'{rect2.area()=}, {rect2.perimetr()=}')
    res_sum = rect1 + rect2
    print(res_sum.side1, res_sum.side2)
    res_sub = rect1 - rect2
    print(res_sub.side1, res_sub.side2)
    help(Rectangle)
