"""Напишите следующие функции:
 - Нахождение корней квадратного уравнения
 - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
 - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
 - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""

import csv
import random
from typing import Callable


def gen_csv():
    with open('gen_num.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data = []
        for i in range(100, 1000):
            my_list = [random.randint(0, 100) for _ in range(3)]
            data.append(my_list)
        csv_write.writerows(data)


gen_csv()


def deco(func: Callable):
    list_res = []
    data_dict = {}
    with open('gen_num.csv', 'r', newline='', encoding='utf-8') as f:
        csv_read = csv.reader(f)
        for row in csv_read:
            for i in row:
                list_res.append(i)

    def wrapper(*args, **kwargs):
        print('Deco start')
        for i in list_res:
            res = i.split()
            a = int(res[0])
            b = int(res[1])
            c = int(res[2])
            res_final = func(a, b, c)
            print(res_final)
            data_dict.update({(a, b, c): res_final})

        data_dict.update(**kwargs)
        print(data_dict)

        print('Deco finish')
    return wrapper


def deco1(func: Callable):
    def wrapper(*args, **kwargs):
        print('Deco1 start')
        data_dict = func({'kw': 5})
        with open('result.json', 'w') as f_json:
            f_json.dump(data_dict, f_json)
        print('Deco finish')
    return wrapper


@deco
def quadratic(a: int, b: int, c: int):
    if a == 0:
        print('Это линейное уравнение, а не квадратное')
    else:
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b + d ** (1 / 2)) / (2 * a)
            x2 = (-b - d ** (1 / 2)) / (2 * a)
            return x1, x2
        elif d == 0:
            return -b / (2 * a)
        else:
            return 'Корней нет'


quadratic()