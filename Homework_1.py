# Task_1
a = int(input('Введите сторону a'))
b = int(input('Введите сторону b'))
c = int(input('Введите сторону c'))
if a + b > c and a + c > b and b + c > a:
    if a == b != c or a == c != b or b == c != a:
        print('Треугольник существует, он РАВНОБЕДРЕННЫЙ')
    elif a == b == c:
        print('Треугольник существует, он РАВНОСТОРОННИЙ')
    else:
        print('Треугольник существует, он РАЗНОСТОРОННИЙ')

else:
    print('Треугольник не существует')

# Task_2
min_limit = 0
max_limit = 100000
f = False
num = int(input(f'Введите число от {min_limit} до {max_limit}: '))
counter = 0
if min_limit < num < max_limit:
    for i in range(2, num+1):
        if num % i == 0 and i != num:
            f = True

    if f:
        print('Число составное')
    else:
        print('Число простое')

else:
    print('Вы ввели неверное число. Введите число от 0 до 100000')


#Task_3
from random import randint
min_lim = 0
max_lim = 1000
num = randint(min_lim, max_lim)
count = 1
while count <= 10:
    print('Попытка', count)
    count += 1
    num_enter = int(input(f'Введите число от {min_lim} до {max_lim}: '))
    if num_enter == num:
        print('Поздравляем вы угадали!')
        break
    elif num_enter < num:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')

else:
    print('Ваши попытки закончилисью. Загаданное число: ', num)

