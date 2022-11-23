# Eg 1
# (*) i.e repition creates clone but not deep clone
a = [[10]]
m = a
b = a*3
b[1][0] = 5
print(b is a)  # False b & m are not pointing to same list

m[0][0] = 20
print(m, b)  # But not depp clone

# Eg 2
# (*=) does inplace job
c = [[10]]
d = c
c *= 3
c[1][0] = 5
print(c is d)  # True i.e c is still modifying original list