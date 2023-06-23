"""Доработаем задачи 5-6. Создайте класс-фабрику.
 - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
 - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики"""


class Animal():
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f'{self.name} {self.weight} {self.age}'


class Bird(Animal):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return "Fly"

    def say(self):
        return self._sound

    def __str__(self):
        return f"{super().__str__()} {self.bird_type}"


class Dog(Animal):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self):
        return "Run"

    def say(self):
        return "Gov"

    def __str__(self):
        return f'{super().__str__()} {self.dog_type}'


class Fish(Animal):
    def __init__(self, name: str, weight: int, age: int, fish_type: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        return "Swim"

    def say(self):
        return ""

    def __str__(self):
        return f"{super().__str__()} {self.fish_type}"


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "Bird":
            return Bird("Гоша", 1, 3, "Попугай", "Чирик")
        elif animal_type == "Dog":
            return Dog("Рэкс", 40, 5, "Такса")
        elif animal_type == "Fish":
            return Fish("Карп", 10, 5, "Речной")
        else:
            return "Неверный тип животного"


if __name__ == '__main__':
    dog = AnimalFactory().create_animal("Dog")
    print(dog)
