import operator
from collections import Counter as ctr
from typing import List
import sys
import itertools as it


def canEitherListBeEaten(l1: list, l2: list):
    """
    Check if l1's elements all are presented in l2's element
    """
    len_l1 = len(l1)
    len_l2 = len(l2)

    if len_l1 > len_l2:
        s, b = l2, l1
    else:
        s, b = l1, l2

    for e in s:
        if s.count(e) > b.count(e):
            break
    else:
        return True
    return False


def minmax(lst: List[int]):
    minimum = lst[0]
    maximum = lst[0]

    for n in lst[1:]:
        if n > maximum:
            maximum = n
        elif n < minimum:
            minimum = n
    return minimum, maximum

# deprecated see second approach down below
def list_intersection(l1, l2):
    l1_ctr = ctr(l1)
    l2_ctr = ctr(l2)
    
    l1_set, l2_set = set(l1), set(l2)
    common_members = l1_set.intersection(l2_set)
    
    if not common_members:
        return []
    
    ans = []
    
    for m in common_members:
        ans.extend(it.repeat(m, min(l1_ctr[m], l2_ctr[m])))

    return ans  

def list_intersection_2(l1, l2):
    '''
        Compelxity -> O(n + m) , n = len(l1) & m = len(l2)
        Using HashMap | HashTable | Dictionary
    '''
    if len(l1) > len(l2):
        s_l, b_l = l2, l1 
    else:
        s_l, b_l = l1, l2 
    freq_s_l = ctr(s_l)
    ans = []
    for n in b_l:
        cnt = freq_s_l.get(n, 0)
        if cnt:
            ans.append(n)
            freq_s_l[n] -= 1
    return ans

def counter(nums):
    ctr = {}
    for e in nums:
        ctr[e] = 1 + ctr.get(e, 0)
    return ctr

def argMax(nums):
    max_idx = max(range(len(nums)), key=nums.__getitem__)
    return max_idx


s = canEitherListBeEaten([13, 12, 3], [2, 2, 12, 13])
print(s)

print(minmax([1, 2, 3, 2, 10, 8, -1]))

print(counter([11,1,2,11,2,3,2,1,22,2,22,5,4,4,4,4,4,4,4,5,5,5,11,1]))

print(argMax([1,2,4,5,3,10,6,8,20,9]))