import itertools as it
# Convert String to List
s = "nipun"
*l, = s


# Get only kth element for
l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
s = [0, 0, 1]
t = zip(*l)
c = next(it.compress(t, s))
print(c)


# Filter the Odd Nums
def filterOddNums(lst):
    *a, = filter(partial(and_, 1), lst)
    return a
