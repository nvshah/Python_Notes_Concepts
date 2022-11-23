#!/bin/python3

import math
import os
import random
import re
import sys
import math
import itertools as it
import operator

# Complete the funnyString function below.
def funnyString(s):
    #get the length of the string
    l_s = len(s)
    #For even number we will have odd number of alternating differences 
    #for odd number we will have even number of alternating differences
    first_cnt = l_s // 2 if l_s % 2 != 0 else l_s // 2 - 1
    #print(first_cnt)
    
    #first half generator of symmetric alternating character difference list
    first_half = (abs(operator.sub(ord(e[0]), ord(e[1]))) for e in zip(s[:first_cnt+1], s[1:first_cnt+1]))

    first_half_alt = map(lambda x, y: abs(ord(x)-ord(y)), s[:first_cnt+1], s[1:first_cnt+1])
    
    #print(first_half)
    
    #first_half = [(e[0], e[1]) for e in zip(*[iter(s[:first_cnt+1])]*2)]
    
    #second half generator of symmetric alternating character difference list
    second_half = (abs(operator.sub(ord(e[0]), ord(e[1]))) for e in zip(s[-1:first_cnt-1:-1], s[-2:first_cnt-1:-1]))

    second_half_alt = map(lambda x, y: abs(ord(x)-ord(y)), s[-1:first_cnt-1:-1], s[-2:first_cnt-1:-1])
    
    #print(second_half)
    
    #print(second_half)
    
    #go from first half left end & 2nd half right(tail) end one by one comparing diff
    #Reason i.e final list i.e [first + second] must be symmetric so checking from left of first & right of second one by one.
    for a,b in zip(first_half, second_half):
        #print(a,b)
        if a != b:
            return 'Not Funny'
    else:
        return 'Funny'
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
