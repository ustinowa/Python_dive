"""Напишите следующие функции:
 - Нахождение корней квадратного уравнения
 - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
 - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
 - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""

import csv
import random
from typing import Callable

import args as args


def quadratic(a: int | float, b: int | float, c: int | float):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** (1/2)) / (2 * a)
        x2 = (-b - d ** (1/2)) / (2 * a)
        return x1, x2
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Корней нет'


def gen_csv():
    with open('gen_num.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data = []
        for i in range(100, 1000):
            my_list = [random.randint(0, 100) for _ in range(3)]
            data.append(my_list)
        csv_write.writerows(data)


gen_csv()
data_dict = {}
with open('gen_num.csv', 'r', newline='', encoding='utf-8') as f:
    csv_read = csv.reader(f)
    list_res = []

    for row in csv_read:
        for i in row:
            list_res.append(i)

for i in list_res:
    res = i.split()
    a = int(res[0])
    b = int(res[1])
    c = int(res[2])
    res1 = quadratic(a, b, c)
    data_dict.update({(a, b, c): res1})
print(data_dict)

# print(data_dict)
# final_dict = {'Решение кв. уравнения:': data_dict}
# print(final_dict)
with open('result.json', 'w') as f_json:
    f_json.dump(data_dict, f_json)

# def data_from_csv() -> Callable:

