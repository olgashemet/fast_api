from dataclasses import dataclass
from typing import List


@dataclass
class User:
    name: str
    profession: str
    age: int = 30
    def calculate_year_of_birth(self):
        year=2023-int(self.age)
        return year

first_person= User('AAA',  'BBB', '30')
print(first_person)
print(first_person.calculate_year_of_birth())

from typing import List


class Person:
    pass


@dataclass
class People():
    people: List[Person]
