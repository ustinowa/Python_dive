import argparse
import logging

import argparse as argparse

FORMAT = "{levelname} - {asctime} - {msg}"
logging.basicConfig(format=FORMAT, style="{", filename='info.log', level=logging.INFO, encoding="UTF-8")
logging.basicConfig(filename='error.log', level=logging.ERROR, encoding="UTF-8")

logger = logging.getLogger(__name__)


def simple_num(num: int):
    min_limit = 0
    max_limit = 100000
    f = False
    num = input(f'Введите число от {min_limit} до {max_limit}: ')
    try:
        num = int(num)
        if min_limit < num < max_limit:
            for i in range(2, num + 1):
                if num % i == 0 and i != num:
                    f = True
            if f:
                res = 'Число составное'
                logger.info(f'{num} - {res}')

            else:
                res = 'Число простое'
                logger.info(f'{num} - {res}')

        else:
            res = 'Вы ввели неверное число. Введите число от 0 до 100000'
            logger.info(res)

    except ValueError as e:
        # return f'Введенно неверное значение {e}\nПопробуйте еще раз!'
        logging.error(f'Введенно неверное значение. Ошибка: {e}')

    return res


if __name__ == '__main__':
    # print(simple_num())
    parser = argparse.ArgumentParser(description='Solving simple numbers')
    parser.add_argument('number', metavar='num', type=int, nargs='*', help='enter number from 0 to 10000')
    args = parser.parse_args()
    print(simple_num(*args.number))
