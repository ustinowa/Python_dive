def fibonachi(x: int):
    num = 0
    num1 = 1
    for _ in range(1, x-1):
        a, num = num, num1
        num1 = a + num1
        yield num1


for i in fibonachi(15):
    print(f'{i}', end=' ')

