"""Function for file renaming"""

import os
from pathlib import Path


def rename_file(name: str | Path, extension: str, new_extension: str, range_str: list):
    count = 1
    for file_name in os.listdir(path='D:\Работа\Обучение GeekBrains\Python_dive\Homework_7'):
        # p = file_name
        n1, suffix1 = file_name.split('.')
        # n, suffix = name.split('.')
        if suffix1.lower() == extension:
            Path(file_name).rename(file_name[range_str[0]:range_str[1]]+name+str(count)+'.'+new_extension)
            count += 1


rename_file('newfile', 'txt', 'pdf', [3, 6])
