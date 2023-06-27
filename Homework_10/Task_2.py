"""Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра."""

from pathlib import Path
from typing import TextIO
import json


def _read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if not line:
        fd.seek(0)
        return _read_or_begin(fd)
    return line[:-1]


class CreateJson:
    def __init__(self, numbers: Path, words: Path, result: Path):
        self.numbers = numbers
        self.words = words
        self.result = result

    def two_files_in_one(self) -> None:
        with (open(self.numbers, 'r', encoding='utf-8') as f_num,
              open(self.words, 'r', encoding='utf-8') as f_word,
              open(self.result, 'w', encoding='utf-8') as f_res
              ):
            len_numbers = sum(1 for _ in f_num)
            len_word = sum(1 for _ in f_word)
            for _ in range(max(len_numbers, len_word)):
                num = _read_or_begin(f_num)
                word = _read_or_begin(f_word)
                num_a, num_b = num.split('|')
                mult = int(num_a) * float(num_b)
                if mult < 0:
                    f_res.write(f'{word.lower()} {abs(mult)}\n')
                elif mult > 0:
                    f_res.write(f'{word.upper()} {round(mult)}\n')

    def create_json(self, file: Path) -> None:
        file_data = {}
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                name, number = line.split(' ')
                file_data[name.capitalize()] = float(number)
        with open(file.stem + '.json', 'w', encoding='utf-8') as f_2:
            json.dump(file_data, f_2, ensure_ascii=False, indent=2)