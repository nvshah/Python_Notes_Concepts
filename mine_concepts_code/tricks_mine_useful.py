# dict minimum based on item val

d = {1: 1, 2: 2, 3: 34, 4: 32, 5: 0, 6: 10}

key_min = min(d, key=d.get)

print(key_min)  # 5

# ------


def slice_iter_assign():
    l = [1, 2, 3, 4, 4, 5]

    # NOTE : We can assign iterator to sliced assignments
    l[2:4] = iter([10, 20])

def filterOddNums(lst):
    *a, = filter(partial(and_, 1), lst)
    return a


# Sort the list of tuple
l = [(1, 2), (2, 0), (2, 4), (3, 3), (3, 10)]

# lower left val & higher right val first
n = sorted(l, key=lambda x: (x[0], -x[1]))

print(n) # [(1, 2), (2, 4), (2, 0), (3, 10), (3, 3)]
