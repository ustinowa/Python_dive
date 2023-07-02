"""
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


def triangle(a: int, b: int, c: int):
    """
    Checking for the existence of a triangle
    >>> triangle(6, 6, 3)
    'Треугольник существует, он РАВНОБЕДРЕННЫЙ'
    >>> triangle(5, 5, 5)
    'Треугольник существует, он РАВНОСТОРОННИЙ'
    >>> triangle(3, 5, 6)
    'Треугольник существует, он РАЗНОСТОРОННИЙ'
    >>> triangle(5, 5, 50)
    'Треугольник не существует'
    >>> triangle(5, 5, '5')
    Traceback (most recent call last):
    ...
    TypeError: '>' not supported between instances of 'int' and 'str'
    """
    if a + b > c and a + c > b and b + c > a:
        if a == b != c or a == c != b or b == c != a:
            return f'Треугольник существует, он РАВНОБЕДРЕННЫЙ'
        elif a == b == c:
            return f'Треугольник существует, он РАВНОСТОРОННИЙ'
        else:
            return f'Треугольник существует, он РАЗНОСТОРОННИЙ'

    else:
        return f'Треугольник не существует'


if __name__ == '__main__':
    import doctest
    # print(triangle(5, 6, 3))
    doctest.testmod(verbose=True)
