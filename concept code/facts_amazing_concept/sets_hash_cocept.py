a = 1
b = 1 + 0j

print(hash(a) == hash(b))  # True
print(a == b)  # True

s = {1, 2, 3}
s.remove(1+0j)
print(s) # {2,3}