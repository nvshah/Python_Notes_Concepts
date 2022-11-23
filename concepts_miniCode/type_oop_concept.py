"""
    To create a BluePrint of Persons (i.e class)
    `type` is the class that will govern it 

    Bluprint that allows you to define classes(custom objects) :- `type` class
    Blueprint that allows you to define your own function :- `function` class
    Blueprint that allows you to define your own method :- `method` class
"""


# 1 -------------- type class in python --------------
class Person:
    """
    Person class is blueprint for creating object of type :- `__main__.Person`
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("Walking...")


def fight():
    pass


p = Person("Nipun", 20)
print(type(p))  # <class '__main__.Person'>
print(type(Person))  # <class 'type'>

print(type(p.walk))  # <class 'method'>
print(type(fight))  # <class 'fucntion'>


# 2 ----------- RUN TIME CREATION OF CLASS BLUEPRINT --------------

# Low-Level Code that python internally does using type() for class Name syntax
# High-Level class name


def animal_init(self, name):
    self.name = name


def run(self):
    print("running {} ...".format(self.name))


TAnimal = type("Animal", (), {"__init__": animal_init, "run": run})
lion = TAnimal("Simba")
print(lion.name)
print(lion.run())
