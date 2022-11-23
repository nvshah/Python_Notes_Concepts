#!/bin/python3

import math
import os
import random
import re
import sys
import string

#que -> https://www.hackerrank.com/challenges/caesar-cipher-1/problem

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    l = len(s)   #length of string
    o = k % 26   # number of rotation to perform on left side ( from right to left )

    small_alphabet_string = string.ascii_lowercase
    small_rotated_string = small_alphabet_string[o:] + small_alphabet_string[:o]
    
    big_alphabet_string = string.ascii_uppercase
    big_rotated_string = big_alphabet_string[o:] + big_alphabet_string[:o]
    
    small_translation = s.maketrans(small_alphabet_string, small_rotated_string)   #mapping after performing o rotation on small alphabets
    big_translation = s.maketrans(big_alphabet_string, big_rotated_string)         #mapping after performing o rotation on big alphabets
    
    #Translating string 
    ans_s = s.translate({**small_translation, **big_translation})
    
    #print(ans_s)
    return ans_s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())

    s = input()
    k = int(input())

    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()
