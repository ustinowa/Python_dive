import pytest


def triangle(a: int, b: int, c: int):
    if a + b > c and a + c > b and b + c > a:
        if a == b != c or a == c != b or b == c != a:
            return f'Треугольник существует, он РАВНОБЕДРЕННЫЙ'
        elif a == b == c:
            return f'Треугольник существует, он РАВНОСТОРОННИЙ'
        else:
            return f'Треугольник существует, он РАЗНОСТОРОННИЙ'

    else:
        return f'Треугольник не существует'


def test_isosceles():
    assert triangle(6, 6, 3) == 'Треугольник существует, он РАВНОБЕДРЕННЫЙ'


def test_equilateral():
    assert triangle(5, 5, 5) == 'Треугольник существует, он РАВНОСТОРОННИЙ'


def test_scalene():
    assert triangle(3, 5, 6) == 'Треугольник существует, он РАЗНОСТОРОННИЙ'


def test_no_triangle():
    assert triangle(5, 5, 50) == 'Треугольник не существует'


def test_value_error():
    with pytest.raises(TypeError):
        triangle(5, 5, '5')


if __name__ == '__main__':
    pytest.main('[-v]')
