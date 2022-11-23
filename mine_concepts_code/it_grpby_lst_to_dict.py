from collections import defaultdict
import itertools as it

# Sorted
l = [(1, 0), (1, 2), (2, 0), (2, 3), (1, 1), (2, 2), (3, 4), (3, 0), (3, 1)]

d_l2 = defaultdict(int)

for e in l:
    d_l2[e[0]] = max(d_l2[e[0]], e[1])

print(d_l2)


# ---------

l_s = sorted(l)
l_g = it.groupby(l_s, key=lambda x: x[0])
l_sg = list(([max(g, key=lambda x: x[1]) for _, g in l_g]))
print(l_sg)
