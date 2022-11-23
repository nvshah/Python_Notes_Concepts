#!/bin/python3

#Que hackerrank.com/challenges/pangrams/problem
import math
import os
import random
import re
import sys

# Complete the pangrams function below.

def normalize_string(string: str) -> str:
    regex = r"\s+"
    subst = ''
    result = re.sub(regex, subst, string)
    
    return result if result else string

def pangrams(s):
    s = normalize_string(s)
    letters = set(s.lower())
    print(letters)
    return 'pangram' if len(letters) == 26 else 'not pangram'


if __name__ == '__main__':
    s = input()

    result = pangrams(s)

    print(result)