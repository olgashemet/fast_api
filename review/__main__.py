import keyword

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


e = 1


def f(x, y, *, z):
    a = x + y + z + e

    debug("NAMESPACE:FUNCTION - GLOBALS", globals())
    debug("NAMESPACE:FUNCTION - LOCALS", locals())

    return a


debug("NAMESPACE:MODULE - GLOBALS", globals())
debug("NAMESPACE:MODULE - LOCALS", locals())

x = 1000
debug("Function Result", f(1, 2, z=3))


class Cat:
    name = "fsfds"

    def __init__(self):
        self.a = 10

        # ...
        debug("NAMESPACE - INSTANCE", self.__dict__)

    def count(self):
        b = 10  # self.a+1

        debug("NAMESPACE:Class - function", locals())

        # ...
        # debug("NAMESPACE - INSTANCE", self.__dict__)
        # ...

        return b

    debug("NAMESPACE:Class", locals())
    print("kekekeke", 1 + 2)


undef = "<undefined>"


def getattr_safe(smth, attr):
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
