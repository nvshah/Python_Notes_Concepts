t1 = (1,2,3)
# 1. Shallow Copy
t2 = tuple(t1)
print(t1 is t2)  # True

# 2. Slice Copy
t3 = t1[:]
print(t3 is t1)  # True



