# Генератор простых чисел
def simple_numbers(number: int):
    if not isinstance(number, int):
        raise TypeError(f'Введите целое число {type(number)=}')
    yield 2
    for i in range(3, number + 1):
        simple = True
        for j in range(2, i - 1):
            if not i % j:
                simple = False
        if simple:
            yield i


print(*simple_numbers(20.3))