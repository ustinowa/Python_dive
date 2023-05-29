
mas_bag = int(input('Введите грузоподьемность рюкзака: '))
dict_bag = {'спички': 1, 'палатка': 2, 'аптечка': 3, 'печенье': 2, 'консервы': 3, 'вода': 5}
print(dict_bag)
sum1 = 0
for value in dict_bag.values():
    for key, value in dict_bag.items():
        if sum1 + value <= mas_bag:
            sum1 = sum1 + value
            print(key)
print('bag_mas = ', sum1)
