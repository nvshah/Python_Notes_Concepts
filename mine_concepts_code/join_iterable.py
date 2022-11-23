#GOAl - join function same ason string to all iterable as well

#def __join__(self, ):

import itertools as it


l = [1]

filler = '-'

#Approach 1 (In-Place) , Works only with list 
def join_inplace(itr :list, filler: object) -> list:
    if len(itr) == 1:
        return
    for i in range(len(l)-1, 0, -1):
        itr.insert(i, filler)

#Approach 2, Works with any iterable
join = lambda itr,filler : [*it.chain.from_iterable(t for t in zip(l, it.repeat(filler, len(l)-1)))] + l[-1:]

join_inplace(l, '-')
m = join(l, '*')
print(m)


