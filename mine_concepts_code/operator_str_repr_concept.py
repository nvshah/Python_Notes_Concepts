from operator import attrgetter


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"STR -> Person -> {self.name} -> {self.age}"

    def __repr__(self) -> str:
        return f"REPR -> Person -> {self.name} -> {self.age}"


p1 = Person("Rohit", 22)
p2 = Person("Kamla", 21)
p3 = Person("Mouni", 23)

print(p2)  #  STR -> Person -> Kamla -> 21

l = [p1, p2, p3]

d2 = sorted(
    l, key=attrgetter("age")
)  # [REPR -> Person -> Kamla -> 21, REPR -> Person -> Rohit -> 22, REPR -> Person -> Mouni -> 23]
print(d2)
