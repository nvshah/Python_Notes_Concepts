import itertools as it
l = [1,2,1,2,1,2,1]

# for i in range(2):
#     print(i)
# else:
#     print(11211)

# for i in it.repeat(2, 2):
#     print(i)
# else:
#     print(12121)

dl = range(len(l))
il = list(it.filterfalse(lambda x: l[x]==1, dl))
print(il)

# g = (i for i in range(5))
# for i in it.repeat(g,5):
#     print(next(i))

# for i in it.dropwhile(lambda x: l[x]==1, dl):
#     print(i)
# else:
#     print(1212121)