#!/bin/python3

import math
import os
import random
import re
import sys
import functools as ft

# Complete the anagram function below.
def anagram(s):
    l = len(s)
    m = l//2
    if l%2 != 0:
        return -1
    s1, s2, s1_set, s2_set = s[:m], s[m:], set(s[:m]), set(s[m:])
    #Find all the unique char in s1, as allunique needs to be replaced
    s1_unique = s1_set - s2_set
    #common between s1 & s2 can be settled 
    common = s1_set.intersection(s2_set)

    give = 0 #no. of extra common characters
    take = 0 #no. of required common character to be replaced

    for e in common:
        d = s1.count(e) - s2.count(e)
        if d<0:
            take += abs(d)
        else:
            give += abs(d)

    common_settlement = min(give, take)    # count no. of give & take that can be intersolved & satisfied
    common_remaining = give - take         # extra common charatcers
    #if there are extra common characters in s1, then we need to replace them as well i.e count them as well 
    left_replacement = common_remaining if common_remaining > 0 else 0
    
    unique_total = sum([s1.count(e) for e in s1_unique])

    return unique_total + common_settlement + left_replacement
    
    
if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = anagram(s)