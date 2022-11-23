#!/bin/python3

from collections import Counter as ctr
from functools import reduce
import operator as op
import itertools as it

# Complete the isValid function below.
def isValid(s):
    chr_cntr = ctr(s)   # count the characters repeatation in string
    chr_cnts = chr_cntr.values()  
    unique_chr_cnts = set(chr_cnts) 
    #As there is no way that all character can be made to have same count 
    if len(unique_chr_cnts) > 2:
        return 'NO'
    if len(unique_chr_cnts) == 1:
        return 'YES'
    # exactly 2 count
        
    #Check if it's possible to loose 1 character so that all character have same counts
    diff = abs(unique_chr_cnts[0] - unique_chr_cnts[1])

    # if diff is 1 then there are chances that we can drop 1 character & all character count then be equalised
    if diff != 1:
        return 'NO'

    group_cnts = ctr(chr_cnts)

    #Either of group must have only 1 member so that if required then it's member can be drop away 
    #check if character can be dropped i.e the character group having unique count must have count larger than other character group counts
    #so that it can drop 1 character 
    #So among unique character count the max count group must be single
    # if 1 not in group_cnts.values() or group_cnts[max(unique_chr_cnts)] != 1:
    #     return 'NO'

    # return 'YES'

    if 1 in group_cnts.values() and group_cnts[max(unique_chr_cnts)] == 1:
        return 'YES'
    
    return 'NO'





    # #unique_chr_cnts = (*unique_chr_cnts)
    # cnt_to_chr_grp = dict(ctr(chr_cnts))

    #     print(cnt_to_chr_grp)
        
    #     # if there are 2 different unique counts then either of them must be 1 inorder suffice that all characters count must be equal 
    #     if max(cnt_to_chr_grp.values()) != reduce(op.mul, cnt_to_chr_grp.values(), 1):
    #         return 'NO'

    #     v = it.cycle(unique_chr_cnts)
    #     d = abs(next(v) - next(v))
    #     if d<=1:
    #         if cnt_to_chr_grp[min(unique_chr_cnts)] < cnt_to_chr_grp[max(unique_chr_cnts)]:
    #             return 'NO'
    #         else:
    #             return 'YES'
    #     else:
    #         return 'NO'

if __name__ == '__main__':

    s = input()

    while s != 'e':

        result = isValid(s)

        print(result)

        s = input()
