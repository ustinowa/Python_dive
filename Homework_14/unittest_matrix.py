import unittest
from doctest_matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_eq(self):
        self.assertFalse(Matrix([[2, 1, 3], [5, 4, 1]]) == Matrix([[4, 3, 5], [5, 6, 0]]))

    def test_add(self):
        self.assertEqual(Matrix([[2, 1, 3], [5, 4, 1]]) + Matrix([[4, 3, 5], [5, 6, 0]]), [[6, 4, 8], [10, 10, 1]])

    def test_mul(self):
        self.assertEqual(Matrix([[1, 2], [3, 4], [5, 6]]) * Matrix([[7, 8, 9], [0, 1, 2]]), [[7, 10, 13], [21, 28, 35], [35, 46, 57]])


if __name__ == '__main__':
    unittest.main(verbosity=True)
