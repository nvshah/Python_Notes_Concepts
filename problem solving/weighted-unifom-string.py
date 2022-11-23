from collections import Counter

#Quehttps://www.hackerrank.com/challenges/weighted-uniform-string/problem

#Attempt 1 ( More time consuming) -------------

# calculate each possible uniform weight of substring in given string i.e { a=1, b=2, c=3, ...,  z=26}
def weightedUniformStrings(s, queries):
    possible_weights = []
    
    chr_cnt = Counter(s)
    for k,v in chr_cnt.items():
        weight = ord(k)-96       # As ascii of 'a' is 97
        possible_weights.extend([weight*i for i in range(1, v+1)])
        
    answer = ('Yes' if q in possible_weights else 'No' for q in queries)
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())   # Number of queries i.e no.s to check

    queries = []

    #query input
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)   #calculate the weights of each character for input string

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()


#-------------------

#Attempt 2 (lesser time)

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import itertools as it

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    possible_weights = set()
    list_of_weights_per_grp = []
    
    groups = {''.join(g) for k,g in it.groupby(s)}
    #print(groups)
    for g in groups:
        weight = ord(g[0])-96
        list_of_weights_per_grp.append({i for i in range(weight, len(g)*weight+1, weight)})
    #print(list_of_weights_per_grp)
    possible_weights = set().union(*list_of_weights_per_grp)
    #print(possible_weights)
    
    answer  = ['Yes' if q in possible_weights else 'No' for q in queries]
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

