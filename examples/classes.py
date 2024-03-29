from devtools import debug

# def func(arg1: float, arg2: float) -> float:
#     return arg1 / arg2
#
#
# такой словарь, что:
# 1. ключи - только строки
# 2. строки состоят из [a-zA-Z_]{1}[a-zA-Z0-9_]*
# ns = {
#     "__doc__": "Hello world from T",
#     "a": 1234,
#     "__truediv__": func,
# }
# T = type("T", (), ns)
# print(T.__truediv__)


class T:
    """Hello world from T"""

    attr = 1000

    def gg(self, arg2: float, arg3: float) -> float:
        print(f"{self=!r}")  # noqa: T201
        print(f"{arg2=!r}")  # noqa: T201
        print(f"{arg3=!r}")  # noqa: T201
        return arg2 / arg3 + self.attr


# TODO:  # noqa
# 1. partial
# 2. MRO
# 3. type
# 4. getattr, setattr, delattr, hasattr
# 5. staticmethod, classmethod


# === 1 ===


class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def meow(self) -> None:
        debug(meow=f"Кот {self.name} ({self.age} лет) мяукает")


class Dog:
    name = "Бобик"


vaska = Cat("Васька", 5)
vaska.meow()

joy = Cat("Джой", 15)
joy.meow()


debug(joy.name)
joy.name = 1  # type: ignore  # some experiments
