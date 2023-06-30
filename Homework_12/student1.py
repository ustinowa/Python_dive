# class Descriptor:
#     def __init__(self, name: str):
#         self.name = name
#
#     def __set_name__(self, owner, name):
#
#         self.param_name = '_' + name
#
#     @property
#     def a(self):
#         return self._a
#
#     @property
#     def b(self):
#         return self._b
#
#     @a.setter
#     def a(self, value):
#         if value > 0:
#             self._a = value
#         else:
#             raise ValueError('a не может быть отрицательной')
#
#     # def __get__(self, instance, owner):
#     #     return getattr(instance, self.param_name)
#     #
#     # def __set__(self, instance, value):
#     #     # self.validate(value)
#     #     setattr(instance, self.param_name, value)
#     #
#     # def __delete__(self, instance):
#     #     raise AttributeError(f'Свойство"{self.param_name}"нельзя удалять')
#
#     def validate(self, value):
#         if not self.param_name.capitalize():
#             raise TypeError(f'Значение{value} должно быть целым числом')

        # if not isinstance(value, int):
        #     raise TypeError(f'Значение{value} должно быть целым числом')
        # if self.min_value is not None and value < self.min_value:
        #     raise ValueError(f'Значение{value} должно быть больше 18 или равно{self.min_value}')
        # if self.max_value is not None and value >= self.max_value:
        #     raise ValueError(f'Значение{value} должно быть меньше {self.max_value}')


class Student:

    def __init__(self, name: str):
        self.name = name

    def __set__(self, owner, name):
        if not self.name.upper():
            raise ValueError("не могу установить атрибут")
        self.param_name = '_' + name

    def __repr__(self):
        return f'Student(name={self.name})'


if __name__ =='__main__':
    std_one = Student('архимед')
    print(f'{std_one   = }')

