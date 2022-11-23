#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the miniMaxSum function below. try to find min and max sum outofgiven combination of list of numbers.
def miniMaxSum(arr):
    c = list(map(sum, itertools.combinations(arr, 4)))
    print(min(c), max(c))
    
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)