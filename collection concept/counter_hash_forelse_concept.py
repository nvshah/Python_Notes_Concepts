#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter as ctr

#Que
#https://www.hackerrank.com/challenges/ctci-ransom-note/problem

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_ctr = ctr(magazine)
    note_ctr = ctr(note)
    
    for n in note:
        if magazine_ctr[n] < note_ctr[n]:
            print('No')
            break
    else:
        print('Yes')
    

if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
