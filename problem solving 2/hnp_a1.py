#!/bin/python3

import math
import itertools as it

def find_indexes_to_be_altered(s):
    l = len(s)
    return {i for i in range(l//2) if s[i] != s[-(i+1)]}

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    str_chrs = list(s)
    idx_req_altered = find_indexes_to_be_altered(s)
    req_alter = len(idx_req_altered)

    #print(idx_req_altered)
    
    l = len(s)
    if l == 1:
        if k:
            return '9'
        else:
            return s
    
    if req_alter and req_alter > k:
        return '-1'
    
    #Make string palindrome first
    for idx in idx_req_altered:
        str_chrs[idx] = str_chrs[-(idx+1)] = str(max(int(s[idx]), int(s[-(idx+1)])))
    
    extra_alterations = k - req_alter

    #print(extra_alterations)
    
    if extra_alterations:
        m = l//2-1 if l%2 == 0 else l//2 #middle index
        #print(m)
        for idx in it.filterfalse(lambda i: str_chrs[i] == '9', range(l//2)):
            #print('idx,', idx)
            if idx in idx_req_altered:
                str_chrs[idx] = str_chrs[-(idx+1)] = '9' #step towards making palindrome
                extra_alterations -= 1  #used 1 extra alterations
            #     #idx_req_altered.remove(idx)
            elif extra_alterations > 1:  # Make string number as large as possible
                str_chrs[idx] = str_chrs[-(idx+1)] = '9'  #make character equal to largest
                extra_alterations -= 2 #used 2 extra alterations 
            #print(str_chrs)
            if not extra_alterations:
                #print(extra_alterations)
                break
        else: #we still have extra alterations left
            #print('sasa')
            if l%2 != 0:
                str_chrs[m] = '9'

    #print(str_chrs)
    return ''.join(str_chrs)

if __name__ == '__main__':

   #len, no_of_repeatation_allowed
    n, k = map(int, input('Enter n, k: ').split())
    s = input('Enter string: ')
    
    while s != 'e':

        hvp = highestValuePalindrome(s, n, k)
        print(hvp)
        
        n, k = map(int, input('Enter n, k: ').split())
        s = input('Enter string: ')
