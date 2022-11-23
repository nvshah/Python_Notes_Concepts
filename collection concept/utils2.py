import re
from typing import Callable
from itertools import chain
from operator import itemgetter

# ---------- Strings ----------

def identity(x): return x


def split_join_merge(string: str, regex: str, on_match, on_nonmatch):
    pass


def expand(lst, map_to_iter):
    """ map + chain -> chaining the elements after applying the [map_to_iter] func to each element 
        expand each element into 0 or more elements inside the list
    """
    return chain.from_iterable(map(map_to_iter, lst))


if __name__ == '__main__':
    l = [{'k1': [1, 2, 4], 'k2': [5, 8, 14]}, 
         {'k1': [21, 22, 24], 'k2': [25, 28, 25]}
        ]

    *m, = expand(l, itemgetter('k1'))  
    print(m)  # [1, 2, 4, 21, 22, 24]

    l2 = [[1,2], [3,4], [100, 200]]
    m2 = list(expand(l2, identity))
    print(m2) # [1, 2, 3, 4, 100, 200]
