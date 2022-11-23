#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import itertools as it

#QUE https://www.hackerrank.com/challenges/game-of-thrones/problem?

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    s_count = Counter(s)
    
    *odd_cnt, = filter(lambda x: s_count[x]%2!=0, s_count)
    #print(odd_cnt)
    count = s_count
    if len(s)%2 == 0:
        return 'YES' if not odd_cnt else 'NO'
    else:
        return 'YES' if len(odd_cnt) == 1 else 'NO'
    
    

if __name__ == '__main__':
    s = input()
    result = gameOfThrones(s)
