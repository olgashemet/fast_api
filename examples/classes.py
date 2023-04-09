from functools import partial


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

#neigher self nor class is explicitly passed as  first argument. I can call them from instanse or from the class
#there is no access to the class variables. cannot access  and cannot modify class state.
#When to use: when you need a utility function that doesn't access any properties of a class but makes sense that it belongs to the class
    @staticmethod
    def new_agg(arg4, arg5):
        return arg4+arg5

#It changes class, not just instance of the clss
    @classmethod
    def new_class_agg(cls):
        T.attr=5
    def new_calculated(self):
        new_attribute_1=self.attr
        new_attribute_2=T.attr
        return new_attribute_1, new_attribute_2


# I have to pass
t = T
print(T.attr)
print(t.attr)
print(t.new_calculated(t))
T.new_class_agg()
print(T.attr)
print(t.attr)
print(t.new_calculated(t))
T.gg(t, 1, 2)
T.gg(T, 1, 2)
t.gg(t, 1, 3)
print("new_agg")
T.new_agg(1,3)
print("new_agg")
t.new_agg(2,4)

print(t.mro())
print(t.__base__)

#class object is superclass  for all other classes
print(object.__base__)
# classes like int hs object class as superclass as well
print(int.__base__)

# I am looking for the attribute name in the class,  if I find it if i do not find it i provide a default value
name = getattr(t, 'name', 'Olga')
print(name)

attr = getattr(t, 'attr', 1000000000000)
print(attr)

print('check')
print(t.__getattribute__(t,'attr'))

# I create a new property of the object new_name and assigned value to it.
# To note that I set a new attribute not only the to instance of the class, but to the whole class
# I have to check it!
setattr(t,'new_name', 'Dima')
print(t.new_name)

next_instance=T
print(next_instance.new_name)

print(vars(T))

new_instance_2=T
print("let's re-assign attr")
print(new_instance_2.attr)
print("let's re-assign attr")
print(new_instance_2.__getattribute__(t,'new_name'))
print(getattr(t,'new_name', 'Olga'))

# delete attribute of the object t. The same it deletes arguments  from the object
delattr(t,'new_name')
print(vars(T))
print(vars(next_instance))
setattr(t, 'new_name', 6 )
delattr(t, 'new_name')
print(hasattr(t, 'new_name1'))



# TODO:  # noqa
# 1. partial
# 2. MRO
# 3. type
# 4. getattr, setattr, delattr, hasattr
# 5. staticmethod, classmethod


def multiple(x, y):
    return x * y


a = partial(multiple, 12)
