#!/bin/python3

import math
import os
import random
import re
import sys
import itertools as it

# Complete the alternate function below.
def alternate(s):
    ans = 0
    characters = set(s)    # Unique character in string
    character_combination =  it.combinations(characters, 2)  #get every combination of 2 character
    
    
    subst_single_combination = ""
    
    #regex_alternating = r"^ab(?:ab)*a?$"
    
    for comb in character_combination:
        #regex- Remove all character except 2 character in comb
        regex_single_combination = r"[^{0}{1}]".format(comb[0], comb[1])
        reduced_string = re.sub(regex_single_combination, subst_single_combination, s)

        #print(reduced_string)

        if reduced_string:
            #regex - match if string contains only alternating characters i.e start from ab
            regex_alternating = r"^{0}{1}(?:{0}{1})*{0}?$".format(reduced_string[0], reduced_string[1])
            #print(regex_alternating)
            m = re.match(regex_alternating, reduced_string)
            if m :
                l = len(reduced_string)
                if l > ans:
                    #length of maximum alternating substring possible for given string s
                    ans = l
                    print(reduced_string)
    
    #print(ans)
    return ans
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
