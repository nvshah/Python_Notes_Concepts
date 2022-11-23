from collections import Counter as ctr
import operator as op
from functools import reduce
import functools


@functools.lru_cache()
def factorial(n):
    if n == 1:
        return 1
    return multiplyAll(range(2,n+1))

def multiplyAll(l):
    return reduce(op.mul, l, 1) 

def find_max_palindrome_cnts(s):
    #count unique number of characters for given substring
    s_ctr = ctr(s)

    l = len(s)

    chr_cnt_1 = 0
    chr_even_fact = []
    chr_odd_fact = []

    for cnt in s_ctr.values():
        if cnt == 1:
            chr_cnt_1 += 1
        elif cnt%2 == 0:
            chr_even_fact.append(factorial(cnt//2))
        else:
            chr_odd_fact.append(factorial(cnt//2))

    if chr_cnt_1 == l :
        return l

    chr_cnt_even = len(chr_even_fact)
    chr_cnt_odd = len(chr_odd_fact)

    total_single_odd_cnt = chr_cnt_odd + chr_cnt_1
    
    #counting permutations for half part of string as palindrome mirros after half part
    chr_even_factorial = multiplyAll(chr_even_fact)
    chr_odd_factorial = multiplyAll(chr_odd_fact)

    #first part(of forming palindrome) total character count
    first_half_palindrome_chr_cnt = (l - total_single_odd_cnt)//2  #remaining pairs in total
    
    first_half_permutation = factorial(first_half_palindrome_chr_cnt)//(chr_even_factorial*chr_odd_factorial)

    total_no_of_possible_palindrome = first_half_permutation * (total_single_odd_cnt or 1)

    return total_no_of_possible_palindrome


#ct = find_max_palindrome_cnts('cabcapacac')

#string 
s = input()
#no. of days
days = int(input())
#l & r are including for string index
index_list = [tuple(map(int, input().split())) for d in range(days)]

for l,r in index_list:
    ct = find_max_palindrome_cnts(s[l-1:r])
    ans = ct % (10**9 + 7)

    print(ans)






    

