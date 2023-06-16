from pathlib import Path
import os
import json
import csv
import pickle


def directory(d_path: Path):
    dir_dict = {}
    # dir_dict1 = {}
    # dir_dict['file'] = []
    fields = ['Name', 'Capital City', 'Largest City', 'Population']
    for dir_path, dir_name, file_name in os.walk(d_path):
        #print(f'{dir_path = }\n{dir_name = }\n{file_name= }\n')

        dir_dict['dir_path'] = dir_path
        dir_dict['dir_name'] = dir_name
        dir_dict['file_name'] = file_name

        with open('file_directory.json', 'w', encoding='utf-8') as f:
            json.dump(dir_dict, f, indent=2, ensure_ascii=False)

        with open('file_directory1.csv', 'w', encoding='utf-8') as f_csv:
            file_writer = csv.writer(f_csv, delimiter=':', lineterminator="\r")
            file_writer.writerows(dir_dict.items())

        with open('file_directory2.pickle', 'wb') as f_pickle:
            pickle.dump(dir_dict, f_pickle)




# size = f.seek(0, os.SEEK_END)


# print(os.listdir())
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(obj)
print(directory('D:\Работа\Обучение GeekBrains\Python_dive'))
