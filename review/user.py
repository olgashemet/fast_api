from dataclasses import dataclass
from typing import List


@dataclass
class User:
    """
    высокая цель: хочу чтобы был класс,
    у инстансов которого были 3 атрибута:
    name, profession, age.
    Хочу чтобы они были обязательные + проверять их тип
    """

    name: str
    profession: str
    age: int = 30

    def calculate_year_of_birth(self):
        year=2023-int(self.age)
        return year

first_person= User('30',  'BBB', 'AAA')
print(first_person)
print(first_person.calculate_year_of_birth())


class Person:
    pass


@dataclass
class People():
    people: list[Person]
