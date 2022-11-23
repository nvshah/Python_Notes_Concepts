class A:
    def __init__(self, v, n) -> None:
        self.v = v
        self.n = n

    def __str__(self) -> str:
        return f'v-> {self.v}'


a3 = A(30, None)
a2 = A(20, a3)
a1 = A(10, a2)
a11 = a1

a5 = A(50, None)
a7 = A(70, a5)

a1.n, a1 = a7, a1.n

print(a1.v, a11.n)
