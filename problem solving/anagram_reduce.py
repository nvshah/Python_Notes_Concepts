#!/bin/python3

import math
import os
import random
import re
import sys
import functools as ft

#Que https://www.hackerrank.com/challenges/anagram/problem?h_r=next-challenge&h_v=zen

# Complete the anagram function below.
def anagram(s):
    l = len(s)
    #print(l)
    m = l//2
    if l%2 != 0:
        return -1
    s1, s2, s1_set, s2_set = s[:m], s[m:], set(s[:m]), set(s[m:])
    #print(s1, s2, s1_set, s2_set)
    s1_unique = s1_set - s2_set
    common = s1_set.intersection(s2_set)
    #print(s1_unique, common)

    give = 0
    take = 0

    for e in common:
        d = s1.count(e) - s2.count(e)
        if d<0:
            take += abs(d)
        else:
            give += abs(d)

    #print(take)
    #print(give)

    common_settlement = min(give, take)
    common_remaining = give - take

    #common_remaining = abs(give-take)

    
    #common_stock = ft.reduce(lambda total, e : s1.count(e)-s2.count(e) + total, common, 0)  
    #common_exchange = ft.reduce(lambda total, e : min(s1.count(e),s2.count(e)) + total, common, 0)
    unique_total = sum([s1.count(e) for e in s1_unique])

    left_replacement = common_remaining if common_remaining > 0 else 0 
    
    #print(f'common: {common_settlement}')
    #print(f'unique: {unique_total}')
    
    # #Extra common to remove will be accounted
    # if common_stock > 0 :
    #     print(unique_total + common_stock)
    # else: #if we need to gain common then it can be accomodated inside unique_replacement if possible i.e common req. is less than uniqe. to replace
    #     print(max(unique_total, -common_stock))
        
    
    # print(unique_total + common_total>0 and common_total,)
    
    # #return max(unique_total, common_total)

    #return (common_stock>0 and unique_total + common_stock) or max(unique_total, -common_stock)

    return unique_total + common_settlement + left_replacement
    

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = anagram(s)
        print(result)