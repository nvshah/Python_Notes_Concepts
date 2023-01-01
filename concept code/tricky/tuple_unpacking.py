from re import S


print(True, True, True == (True, True, True))  # True, True, False

print((True, True, True) == (True, True, True)) # True

### Pattern UnPacking

a, (b, c) = (1, (2, 3))
# a = 1, b=2, c=3

a, (b, *c) = (1, (10, 20, 30))
# a=1, b=10, c=[20, 30]

