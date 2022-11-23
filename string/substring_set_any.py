#!/bin/python3

import math
import os
import random
import re
import sys

#Que https://www.hackerrank.com/challenges/two-strings/problem

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    
    s1_s = set(s1)
    s2_s = set(s2)
    
    #Approcah 1  - naive using set intersection
    print('YES' if len(s1_s.intersection(s2_s)) > 0 else 'NO')

    #Approach 2 as we not require all common this can be sometime useful
    return 'YES' if any(s in s2_s for s in s1_s) else 'NO'
    
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
