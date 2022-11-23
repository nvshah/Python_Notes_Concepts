# tips.py
from copy import copy

# create object from type dynamically


class A:
    def __init__(self):
        self.a = 10


class B:
    def __init__(self):
        self.b = 20


def cloneObj(obj):
    return type(obj)()


if __name__ == '__main__':
    o1 = A()
    o2 = copy(o1)
    o3 = cloneObj(o1)

    print(o2.a)
    print(o3.a)
