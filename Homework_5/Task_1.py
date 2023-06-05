def dict_path(link: str) -> tuple:
    prefix, *path1, suffix = link.split('/')
    n, s = str(suffix).split('.')
    p = '/'.join(path1)

    return (f'Путь к файлу: {p}, \nИмя файла: {n}, \nРасширение файла: .{s}')

print(dict_path('D:/Работа/Обучение GeekBrains/Python_dive/Homework_1.py'))
