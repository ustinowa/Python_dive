import decimal


def in_(summ, counter):
    summ_add = decimal.Decimal(input('Введите сумму пополнения: '))
    if summ_add % 50 == 0:
        summ += summ_add
        counter += 1
        if counter == 3:
            summ = summ * decimal.Decimal(1.03)
            counter = 0

    else:
        print('Сумма пополнения должна быть кратна 50')
    print('Баланс счета = ', summ)

def out_(summ, counter):
    summ_get = decimal.Decimal(input('Введите сумму снятия: '))
    summ_proc = summ_get * decimal.Decimal(0.15)
    if 30 < summ_proc < 600:
        summ_get = summ_get + summ_proc
    elif summ_proc < 30:
        summ_get = summ_get + 30
    elif summ_proc > 600:
        summ_get = summ_get + 600
    summ = summ - summ_get
    counter += 1
    if counter == 3:
        summ = summ * 1.03
        counter = 0
    print('Сумма к снятию = ', summ_get)
    print('Баланс счета = ', summ)

summ = decimal.Decimal(0)
counter = 0
while True:
    operation = int(input('Выберите действие:\n1 - Пополнить\n2 - Снять\n3 - Выйти\n'))
    if operation == 1:
        in_(summ, counter)

    if operation == 2:
        out_(summ, counter)

    if operation == 3:
        print('Баланс счета = ', summ)
        break