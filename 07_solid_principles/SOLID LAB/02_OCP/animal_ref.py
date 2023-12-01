from abc import ABC

from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return 'meow'


class Dog(Animal):
    def make_sound(self) -> str:
        return 'woof-woof'


class Turtle(Animal):
    def make_sound(self) -> str:
        return 'turtle sound'


class Chicken(Animal):
    def make_sound(self) -> str:
        return 'cluck-cluck'


def animal_sound(animals: List[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Turtle(), Chicken()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
