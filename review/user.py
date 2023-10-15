from dataclasses import dataclass

from devtools import debug


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

    def calculate_year_of_birth(self) -> int:
        year = 2023 - int(self.age)
        return year


first_person = User(
    age=30,
    profession="BBB",
    name="AAA",
)
debug(first_person)
debug(first_person.calculate_year_of_birth())


class Person:
    pass


@dataclass
class People:
    people: list[Person]
