b1 = 1 + 1 or 0
print(b1)  # 2

b2 = 0 or False or []
print(b2)  # []


def call(exp):
    print("call-> ", exp)
    return exp


# Logical vs BitWise Operator

logical1 = call(10) or call(0)  # lazily
print(logical1)  #

bitwise1 = call(10) | call(0)  # eagerly
print(bitwise1)
