#!/bin/python3

from collections import Counter as ctr
import os

#QUE https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

# Complete the isValid function below.
def isValid(s):
    chr_cntr = ctr(s)   # count the characters repeatation in string
    chr_cnts = chr_cntr.values()  
    unique_chr_cnts = (*set(chr_cnts),)
    #As there is no way that all character can be made to have same count 
    if len(unique_chr_cnts) > 2:
        return 'NO'
    if len(unique_chr_cnts) == 1:
        return 'YES'
    
    # exactly 2 count Scenario from onwards
    
    #For each unique character cnts how much group hold that same count can be found via this map
    chrCnts_to_grpCnts = ctr(chr_cnts)
    
    #------there must be only 1 group from which charatcer can be removed
    
    # or min unique character cnts must be 1 with single corresponding group i.e entire group can be removed as we need to remove single character to vanish off entire group  
    if chrCnts_to_grpCnts.get(1, -1) == 1:
        return 'YES'
    
    # having said that the max character cnts group no. must be 1 so that character can be droped from that group
    if chrCnts_to_grpCnts[max(unique_chr_cnts)] == 1:
        diff = abs(unique_chr_cnts[0] - unique_chr_cnts[1])
        if diff == 1:
            return 'YES'
    
    return 'NO' 


if __name__ == '__main__':

    s = input()

    result = isValid(s)

    print(result)
