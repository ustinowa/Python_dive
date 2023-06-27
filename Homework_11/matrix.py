"""Создайте класс Матрица. Добавьте методы для:
 - вывода на печать,
 - сравнения,
 - сложения,
 - *умножения матриц"""


class Matrix:
    def __init__(self, matrix: list[int]):
        self.matrix = matrix

    def __eq__(self, other):

        f = True
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    f = False
        return f

    def __add__(self, other):
        rows_self = len(self.matrix)
        cols_self = len(self.matrix[0])
        rows_other = len(other.matrix)
        cols_other = len(other.matrix[0])
        if cols_self == cols_other and rows_self == rows_other:
            matrix_result = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    res = self.matrix[i][j] + other.matrix[i][j]
                    matrix_result.append(res)
            return matrix_result
        else:
            return f'Количество строк и столбцов в матрице \n{matrix_a}\nне соответствует количеству строк и столбцов в матрице' \
                   f' \n{matrix_b}\nНельзя складывать!!!'

    def __mul__(self, other):
        rows_self = len(self.matrix)
        cols_self = len(self.matrix[0])
        rows_other = len(other.matrix)
        cols_other = len(other.matrix[0])
        if cols_self == rows_other:
            result = [[0 for row in range(cols_other)] for col in range(rows_self)]

            for s in range(rows_self):
                for j in range(cols_other):
                    for k in range(cols_self):
                        result[s][j] += self.matrix[s][k] * other.matrix[k][j]
            return result
        else:
            return f'Количество столбцов в матрице \n{matrix_a}\nне соответствует количеству строк в матрице ' \
                   f'\n{matrix_b}\nНельзя перемножать!!!'

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])



matrix_a = Matrix([[2, 1, 3], [5, 4, 1]])
matrix_b = Matrix([[4, 3, 5], [5, 6, 0]])
print(matrix_a)
print()
print(matrix_b)
print(f'{matrix_a == matrix_b = }')
matrix_res_mul = matrix_a * matrix_b
matrix_res_sum = matrix_a + matrix_b
print('Сумма матриц = ', matrix_res_sum)
print('Произведение матриц = ', matrix_res_mul)


