import keyword
from typing import Any

from devtools import debug


def is_identifier(value: str) -> bool:
    if value == "":
        return False

    if value[0].isdigit():
        return False

    if not value.isascii():
        return False

    if " " in value:
        return False

    if keyword.iskeyword(value):
        return False

    return True


assert not is_identifier("1a")
assert is_identifier("a1")
assert not is_identifier("")
assert is_identifier("__str__")
assert is_identifier("_")
assert is_identifier("_____________________")
assert is_identifier("_____________________1")
assert not is_identifier("_сяыа")
assert not is_identifier("сяыа")
assert not is_identifier("a a")
assert not is_identifier("a     a")
assert is_identifier("_1")
assert is_identifier("_fsd")
assert not is_identifier("1")
assert not is_identifier("for")
assert not is_identifier("while")


EEE = 1


def f(x: float, y: float, *, z: float) -> float:  # noqa: VNE001
    result = x + y + z + EEE

    debug("NAMESPACE:FUNCTION - GLOBALS", globals())
    debug("NAMESPACE:FUNCTION - LOCALS", locals())

    return result


debug("NAMESPACE:MODULE - GLOBALS", globals())
debug("NAMESPACE:MODULE - LOCALS", locals())

some_x = 1000
debug("Function Result", f(1, 2, z=3))


class Cat:
    name = "fsfds"

    def __init__(self) -> None:
        self.a = 10

        # ...
        debug("NAMESPACE - INSTANCE", self.__dict__)

    def count(self) -> int:
        num = 10  # self.a+1

        debug("NAMESPACE:Class - function", locals())

        # ...
        # debug("NAMESPACE - INSTANCE", self.__dict__)
        # ...

        return num

    debug("NAMESPACE:Class", locals())
    debug("kekekeke", 1 + 2)


undef = "<undefined>"


def getattr_safe(smth: object, attr: str) -> Any:
    try:
        return getattr(smth, attr)
    except AttributeError:
        return undef


instance = Cat()

debug(
    Cat.count,
    instance.count,
    instance,
)

instance.count()
Cat.count(instance)
