import fractions
import math

a = input('Введите первую дробь: ').split('/')
b = input('Введите первую дробь: ').split('/')

nok = (int(a[1]) * int(b[1])) // math.gcd(int(a[1]), int(b[1]))

res_sum = print(int(int(a[0])*(nok/int(a[1]))+int(b[0])*(nok/int(b[1]))),'/',nok)
res_mult = print(int(a[0])*int(b[0]),'/',int(a[1])*int(b[1]))

print('Проверка:')
f1 = fractions.Fraction(int(a[0]),int(a[1]))
f2 = fractions.Fraction(int(b[0]),int(b[1]))
print(f1+f2)
print(f1*f2)