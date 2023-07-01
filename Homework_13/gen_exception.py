import random as rnd


class CustomException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Число должно быть целым и больше нуля. Вы ввели {type(self.value)}, со значением {self.value}'


def gen_fnc(low: int = 1, hight: int = 50, try_count: int = 5) -> bool:
    if not isinstance(low, int):
        raise CustomException(low)
    if not isinstance(hight, int):
        raise CustomException(hight)
    if not isinstance(try_count, int):
        raise CustomException(try_count)

    result = False
    num = rnd.randint(low, hight + 1)

    serch_count = 0
    while serch_count < try_count:
        ask_value = int(input(f"Введите число от {low} до {hight}: "))
        if ask_value == num:
            print("Вы угадали")
            result = True
            break
        if ask_value < num:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
        serch_count += 1
    else:
        print("Попытки закончились")

    return result


if __name__ == '__main__':
    gen_fnc(2, 'string', 3.1)