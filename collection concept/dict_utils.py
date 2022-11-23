import operator as op


def unionAll(*sets):
    return set().union(*sets)


def intersectAll(*sets):
    return unionAll(*sets).intersection(*sets)


def dict_equal_sensative(d1, d2):
    ''' Compare 2 Dictionary (order wise))'''
    # 1. Check First if both dictionary have same items
    if d1 == d2:
        # 2. check if all keys in both dict are in same order
        return all(map(op.eq, d1, d2))
    else:
        return False


def inverse_mapping(f):  # Assuming the {f} is dict
    return f.__class__(map(reversed, f.items()))
    # dict(((v, k) for k, v in f.items()))


def sort_dict_by_values(d, reverse=False):
    return dict(sorted(d.items(), key=op.itemgetter(1), reverse=reverse))


def intersect_dict(d1, d2):
    '''
    Return new dict with common keys & vals as tuple of combined elements
    '''
    common_keys = d1.keys() & d2.keys()
    return {k: (d1[k], d2[k]) for k in common_keys}


def merge_dict(*dict, agg=op.add):
    '''
    merge the dict via aggregator [agg]
    return new dictionary

    : param agg: needs to be function that accept 2 params & return 1 val
    '''
    mergedDict = {}  # ! Note : this merged dict will be unsorted
    for d in dict:
        for k, v in d.items():
            mergedDict[k] = agg(mergedDict.get(k, 0), v)
    return mergedDict


def merge_dict(*dictionaries, agg=op.add, sorted=False, reverse=False):
    '''
    merge the dict via aggregator [agg]
    return new dictionary

    : param agg: needs to be function that accept 2 params & return 1 val
    '''
    # 1. Merge
    mergedDict = {}  # ! Note : this merged dict will be unsorted
    for d in dictionaries:
        for k, v in d.items():
            mergedDict[k] = agg(mergedDict.get(k, 0), v)
    if not sorted:
        return mergedDict

    # 2. Sort
    smd = sort_dict_by_values(
        mergedDict, reverse=reverse)  # sorted merged dict

    return smd


def sym_diff(*maps):
    ''' Symmetric diff of all dicts '''
    res = {}  # symmetric diff
    u = set().union(*maps)  # union all
    i = u.intersection(*maps)  # intersection all
    sd = u - i   # symmetric diff  keys

    res = {k: [m.get(k, 0) for m in maps] for k in sd}  # symmetric diff dicts
    return res


def dict_zip(*dicts):
    if not dicts:
        return

    first = dicts[0]
    rest = dicts[1:]

    n = len(first)
    if any(len(d) != n for d in rest):
        raise ValueError('arguments must have the same length')

    for k, v1 in first.items():
        yield k, v1, *(other[k] for other in rest)


def dict_zip_intersection(*dicts):
    if not dicts:
        return

    keys = set(dicts[0]).intersection(*dicts[1:])

    for k in keys:
        yield k, *(d[k] for d in dicts)


def dict_zip_union(*dicts, fillvalue=None):
    if not dicts:
        return

    keys = set(dicts[0]).union(*dicts[1:])

    for k in keys:
        yield k, *(d.get(k, fillvalue) for d in dicts)


def dict_from_keys_values(keys, values):
    return dict(zip(keys, values))


# ----------------------- TEST ------------------


def inp1():
    # 1. Sort the Dict by Vals
    d = {1: 20, 2: 100, 3: 1, 4: 15}
    sd = sort_dict_by_values(d)

    print(sd)  # {3: 1, 4: 15, 1: 20, 2: 100}

    # 2. Intersect the Dict
    d1 = {1: 10, 2: 20, 3: 30, 6: 60}
    d2 = {1: 100, 4: 400, 5: 500, 6: 600}

    cd = intersect_dict(d1, d2)
    print(cd)  # {1: (10, 100), 6: (60, 600)}

    # 3. Merge Dictionaries
    d1 = {'python': 10, 'java': 20, 'dart': 30, 'c#': 60}
    d2 = {'python': 100, 'kotlin': 400, 'c++': 500, 'c#': 600}
    md = merge_dict(d1, d2, sorted=True, reverse=True)

    print(md)


def inp2():
    d1 = {'e1': 100, 'e2': 200, 'u1': 150, 'u2': 300}
    d2 = {'e1': 350, 'u1': 260, 'u2': 80}
    d3 = {'e1': 180, 'u1': 360, 'l1': 20}

    d = sym_diff(d1, d2, d3)
    print(d)


def check_dict_zip():
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 10, 'b': 20}

    for k, *v in dict_zip(d1, d2):
        print(k, *v)


if __name__ == '__main__':

    # inp2()

    check_dict_zip()
