#!/bin/python3

import math
import os
import random
import re
import sys

#QUE - https://www.hackerrank.com/challenges/reduced-string/problem

# Complete the superReducedString function below.
def superReducedString(s):
    pattern = r'([a-z])\1'
    while(True):
        reduced_string = re.sub(pattern, '', s)
        if reduced_string == s:
            break
        s = reduced_string
    
    return reduced_string if reduced_string else 'Empty String'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
