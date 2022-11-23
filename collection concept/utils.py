from math import isqrt
import itertools as it
from collections import Counter
from string import digits
from textwrap import fill
from functools import reduce
import heapq
from typing import List
from math import log10


def all_equal1(iterable):
    g = it.groupby(iterable)
    return next(g, True) and not next(g, False)

def all_equal2(lst):
    c = Counter(lst)
    return c[lst[0]] == len(lst)


def segregate_into_groups(lst, grpSize=2):
    ''' Eg -> 
          lst = [1,2,3,4,5] 
          size = 2 
          => ans := [(1,2), (3,4), (5, None)] 
    '''
    lst_iter = iter(lst)
    return it.zip_longest(*it.repeat(lst_iter, grpSize), fillvalue=None)

def segregate_into_groups2(lst, grpSize=2):
    ''' Eg -> 
          lst = [1,2,3,4,5] 
          size = 2 
          => ans := [[1,2], [3,4], [5, None]] 
    '''
    full, remain = divmod(len(lst), grpSize)
    f = full*grpSize  # index till full groups

    # Group down the full possible groups
    res = [lst[i:i+grpSize] for i in range(0, f, grpSize)]
    
    if remain: # (Edge Case to fill empty Slots with None)
        res.append([*lst[f:], *[None]*(grpSize-remain)])
    
    return res

def grp_by_offset(lst, gSize):
    ''' Segregat a list into groups (of length gSize) from left -> right 
    Eg  lst := [1,2,3,4,5,6,7,8,9]
        gSize := 3

        out := [(1,2,3), (4,5,6), (7,8,9)]
    '''
    r = it.repeat(iter(lst), gSize)
    z = it.zip_longest(*r, None)
    return z


def argsort(l, mapper, reverse=False):
    '''
        :param l: -> can be any object that cann be indexed (ie list, array, dictionary, tuple)
        :param mapper: -> applied to each element of original arr {l} to extract new element
                          if None then original element will be used itself
                          mapper takes 1 arg & return a val
                          mapper :- is kinda ValueChanged typedef alike 
        :param fun: -> fun to be applied on entire mapped list {ml} after mapper is applied to all elem
        :returns arr: array of indexes where each element-val-idx corresp to element in original array {l}

    '''
    ml = l 
    if mapper:
        ml = list(map(mapper, l))
    return sorted(range(len(l)), key=ml.__getitem__, reverse=reverse)

def rev(arr, l, r):
    '''reverse the arr inplace from [l,r]'''

    def a1():
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l+1, r-1
    
    def a2():
        arr[l:r+1] = reversed(it.islice(arr, l, r+1))

def rotate(nums: List[int], k: int) -> None:
    """
    In-Place Rotation (3 Reversal Approach)
    """
    s = len(nums)  # size
    e = k % s   # effective rotate
    if not e: return  # effectively no change in {nums} after {k} rotation

    nums.reverse()     # 1s Reverse Entire Array
    rev(nums, 0, e-1)  # 2 reverse the first part
    rev(nums, e, s-1)  # 3 reverse the second part

def get_digits(n, key, rev=False):
    if rev:  # In reverse manner ie from LSB -> MSB
        while n:
            n, r = divmod(n, 10)
            yield r if not key else key(r)
    else: # from MSB -> LSB
        digits = int(log10(n))
        for i in range(digits):
            d, n = divmod(n, pow(10, digits-1))
            yield d if not key else key(d)

def lst_to_matrix(lst):
    ''' Convert list of elements of n^2 length -> n*n matrix '''
    s = len(lst)
    d = isqrt(s)
    assert d * d == s, "Provide list of leength that is whole squared"
    r = it.repeat(iter(lst), d)
    *z, = zip(*r)
    return z

def get_boundaries(matrix):
    ''' Get All Boundaries Cells Position of {matrix} 
    ie First & last Rows  &
       First & last Cols

    '''
    m, n = len(matrix), len(matrix[0])

    h = it.product((0, m-1), range(n))  # Horizontal - Rows as Boundary
    v = it.product(range(m), (0, n-1))  # Vertical - cols as Boundary

    bounds = it.chain(h, v)

    return bounds


def inp1():
    l = [1,2,3,4,5]
    # t1, t2 = it.repeat(iter(l), 2)

    # print(next(t1))
    # print(next(t2))

    *t, = segregate_into_groups(l, 1)
    print(t)

    t2 = segregate_into_groups2(l, 1)
    print(t2)


    # ------

    a = [1, 10, 20, 40, 22, 15]
    n = argsort(a, lambda x: abs(x-20))
    print(n)  # [2, 4, 5, 1, 0, 3]

def inp2():
    n = 16 # size
    l = [i for i in range(1, n+1)]  # 3*3
    a = lst_to_matrix(l)
    print(a)

    l2 = [i for i in range(20)]
    b = grp_by_offset(l2, 4)
    print(list(b))

if __name__ == '__main__':
    #all_equal2([2,2,2])

    inp2()

    
  
