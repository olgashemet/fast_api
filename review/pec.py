class Cat:
    age = "3"

    def __init__(self):
        # self.age=5

        print("cat is created")

    def set_name(self, name):
        self.name = name

    def __str__(self):
        print(self.__dict__)
        return f"it is a {self.__class__.__name__} {self.name}"


cat = Cat()
print(cat.__dict__)
cat.set_name("Meya")
print(cat)
##represents a dictionary or any mapping object that is used to store the attributes of the object. Why not age ?
print(cat.__dict__)


# cat.change_name='Murka'
# print(cat)

# class Dog:
#     def __init__(self) -> None:

#         print(" dog is created")

#     def __str__(self):

#         return f"it is a {self.__class__.__name__}   {self.name}"


# cat = Cat()
# cat_2=Cat()
# dog=Dog()
# print(cat.__dict__)
# print(cat_2.__dict__)

# # cat.name='Vasilij'
# #init, class, 21
# cat.__enter__=1
# cat_2.name='Murka'
# cat_2.color='white'
# dog.name='Barbos'
# cat.__str__('murka')

# print(cat.__dict__)
# print(cat_2.__dict__)

# print(cat)
# print(dog)
# print(cat_2)
# print("111")

# print(Cat.__str__(dog))
# print(Cat.__str__)

# x = type('y', (), {})()
# y=x.__class__()
# y.name='CDE'
# x.name = 'ABC'

# print('new dog')
# print(Cat.__str__(self=x))
# print(Cat.__str__(self=y))
# print(cat.__str__())
# print('new dog')
# # bound methd = function of the class (self=instance)
# print(cat.__enter__)
# print(cat.name)

# print('dir(x)')
# print(dir(x))
# print(x)
