#!/bin/python3

import math
import os
import random
import re
import sys
import itertools as it
import functools as ft

#Que https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    l = len(s)       # length of string
    m = l//2         # middle index of string
    s1 = s[:m]       # first part of string
    s2 = s[-1:m-1:-1] if l%2==0 else s[-1:m:-1] # 2nd part of string (neglecting middle element)
    
    #1st attempt
    chr_modi = filter(lambda x: x[0] != x[1], [pair for pair in zip(s1, s2)])  # get all pairs that needs to be change inorder to make string palindrome
     
    cnt = ft.reduce(lambda x,y: x + abs(ord(y[0])-ord(y[1])), chr_modi, 0)  # cnt & add required steps to make string palindrome
    
    #print(cnt)
    
    #2nd attempt
    # while s1 and s1 != s2:
    #     cnt += abs(ord(s1[0]) - ord(s1[1]))
    #     s1 = s1[1:]
    #     s2 = s2[1:]

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
