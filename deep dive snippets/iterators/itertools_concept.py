import itertools as it 
import math
from functools import reduce
import operator as op

# 1 islice amazing concept

def factorials():
    i = 1
    while True:
        print('-> yielding ', i)
        yield math.factorial(i)
        i += 1

l = list(it.islice(factorials(), 2, 5))
#print(l)
''' (Output)notice factorials() is iterated from 0 -> 5 entirely, though we demanded 2 -> 5
-> yielding  1
-> yielding  2
-> yielding  3
-> yielding  4
-> yielding  5
[6, 24, 120]
'''

# Numerical or Float Step-Size
l = it.count(3, 0.5)  # -> returns iterator so no need to call iter()
l2 = [next(l) for _ in range(3)]  

#print(l2)  # [3, 3.5, 4.0]


# Another way 
l = it.count(3, 0.5)
print(*it.islice(l, 3))  # 3 3.5 4.0   //Equivalent ob above but much concise way


# reduce vs accumulate

l = [2,5,10,20,25]
r = reduce(op.add, l)
a = it.accumulate(l)  # All intermediate results in finding reduce()

#print(r)   # 62
#print(*a)  # 2 7 17 37 62

# Amazing groupby concept, 

l = [1,1,1,2,2,2,3,3,3,1,1,2,2,4,4,4,5,5]
ln = sorted(l)
g = iter(l)  # iterator
packed = it.groupby(g)  # uses actual g underhood

for k, v in packed:
    print(k, list(v))

''' OUTPUT
1 [1, 1, 1]
2 [2, 2, 2]
3 [3, 3, 3]
1 [1, 1]
2 [2, 2]
4 [4, 4, 4]
5 [5, 5]
'''
#print(list(g)) # []  // Empty as its consumed by groupby actually

#--------------------------

# Mix Concept - product, tee, count, takewhile

def hyper_grid_range(start, end, stride, dimen=2):
    '''
    generate the hyper grid of dimension {dimen}
    @param start := start val (float)
    @param end := end val (float)
    @param stride := step val (float)
    @param dimen := dimension or column number (int)

    NOTE :- first element will be (smallest, smallest, ...)
            last element will be  (largest, largest, ...)
    '''
    axis = it.takewhile(lambda x: x < end, it.count(start, stride))
    cols = it.tee(axis, dimen)
    grid = it.product(*cols)    # Cross Product

    return grid 


g1 = list(hyper_grid_range(1.5, 10, 4.5, 3))
for r in g1:
    print(r)


#  --------------
