def tr_matrix(lst: list) -> list:
    matrix_t = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            i1, j1 = j, i
            matrix_t.append(lst[i1][j1])

    return matrix_t


matrix = [[1, 2, 7],
          [5, 10, 8],
          [8, 5, 3]]
print(tr_matrix(matrix))

