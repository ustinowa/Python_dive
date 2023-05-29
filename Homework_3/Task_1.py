
my_list = [2, 4, 4, 5, 7, 7, 6, 5]
my_list1 = []
for i in my_list:
    if my_list.count(i) > 1 and i not in my_list1:
        my_list1.append(i)
print(my_list1)
