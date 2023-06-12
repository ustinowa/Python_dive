def chess() -> bool:
    n = 8
    i_list = []
    j_list = []
    print('Введите координаты фигуры через пробел: ')

    for i in range(n):
        new_i, new_j = [int(s) for s in input().split()]
        board[new_i][new_j] = ' Q'
        i_list.append(new_i)
        j_list.append(new_j)

    for i in range(n):
        for j in range(i+1, n):
            if i_list[i] == i_list[j] or j_list[i] == j_list[j] or abs(i_list[i] - i_list[j]) == abs(j_list[i] - j_list[j]):
                return False
            else:
                return True


board = [[11, 12, 13, 14, 15, 16, 17, 18],
         [21, 22, 23, 24, 25, 26, 27, 28],
         [31, 32, 33, 34, 35, 36, 37, 38],
         [41, 42, 43, 44, 45, 46, 47, 48],
         [51, 52, 53, 54, 55, 56, 57, 58],
         [61, 62, 63, 64, 65, 66, 67, 68],# по диагонали i+1, j+1, в строку i остается j+1, в столбец наоборот
         [71, 72, 73, 74, 75, 76, 77, 78],
         [81, 82, 83, 84, 85, 86, 87, 88]]

print(chess())
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=' ')
    print()
