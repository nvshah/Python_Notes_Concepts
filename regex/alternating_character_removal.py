#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/alternating-characters/problem

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    regex = r"([AB])\1+"
    subst = "\\1"
    
    result = re.sub(regex, subst, s)
    
    return len(s) - len(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
