num = int(input('Введите число: '))
n = num
ns = 16  # numeral system - система счисления

res: str = ''
while num > 0:
    re = str(num % ns)
    match re:
        case '10': re = 'A'
        case '11': re = 'B'
        case '12': re = 'C'
        case '13': re = 'D'
        case '14': re = 'E'
        case '15': re = 'F'

    res = re + res
    num = num // ns
print('В ', ns, '-ричной системе счисления равно', res)

print(f'{n: 0x}')
