import unittest
from doctest_triangle import triangle


class TestTriangle(unittest.TestCase):
    def test_isosceles(self):
        self.assertEqual(triangle(6, 6, 3), 'Треугольник существует, он РАВНОБЕДРЕННЫЙ')

    def test_equilateral(self):
        self.assertEqual(triangle(5, 5, 5), 'Треугольник существует, он РАВНОСТОРОННИЙ')

    def test_scalene(self):
        self.assertEqual(triangle(3, 5, 6), 'Треугольник существует, он РАЗНОСТОРОННИЙ')

    def test_no_triangle(self):
        self.assertEqual(triangle(5, 5, 50), 'Треугольник не существует')

    def test_value_error(self):
        self.assertRaises(TypeError, triangle, (5, 5, '5'))


if __name__ == '__main__':
    unittest.main(verbosity=True)
