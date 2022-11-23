from collections import Counter as ctr
import operator as op
from functools import reduce
import functools



# def factorial(n):
#     #return reduce(op.mul,range(1,n+1))
#     return multiplyAll(range(1,n+1))

# @functools.lru_cache(maxsize = 100)
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
@functools.lru_cache(maxsize = 100)
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

    
    #seperate out character with count 1
    chr_1 = list(filter(lambda v: v == 1, s_ctr.values()))
    chr_cnt_1 = len(chr_1)

    if chr_cnt_1 == l :
        return l

    #seperate out character with even count
    chr_even = list(filter(lambda v:v%2 == 0, s_ctr.values()))
    chr_cnt_even = len(chr_even)

    #seperate out character with odd count more than 1 character
    chr_odd = list(filter(lambda v: v!=1 and v%2!=0, s_ctr.values()))
    chr_cnt_odd = len(chr_odd)

    #seperate out character with odd cnt greater than 1
    #chr_cnt_odd = l - (chr_cnt_1 + chr_cnt_even)

    #total pairs count
    #total_pairs_cnt = l - chr_cnt_1

    #total_single_odd_cnts
    total_single_odd_cnt = chr_cnt_odd + chr_cnt_1
    
    #counting permutations for half part of string as palindrome mirros after half part
    chr_even_factorial = multiplyAll(map(lambda c: factorial(c//2), chr_even))
    chr_odd_factorial = multiplyAll(map(lambda c: factorial(c//2), chr_odd))

    #first part(of forming palindrome) total character count
    first_half_palindrome_chr_cnt = (l - total_single_odd_cnt)//2  #remaining pairs in total

    #first_half_permutation = factorial(first_half_palindrome_chr_cnt)/(chr_even_factorial * chr_odd_factorial)
    #max_of_divisor = max(chr_even_factorial, chr_odd_factorial)
    #min_of_divisor = min(chr_even_factorial, chr_odd_factorial)

    #print(first_half_palindrome_chr_cnt, chr_even_factorial, chr_even)
    
    first_half_permutation = factorial(first_half_palindrome_chr_cnt)//(chr_even_factorial*chr_odd_factorial)
    #first_half_permutation = multiplyAll(range(first_half_palindrome_chr_cnt,max_of_divisor,-1))//factorial(min_of_divisor)

    #print(first_half_permutation)

    total_no_of_possible_palindrome = first_half_permutation * (total_single_odd_cnt or 1)

    #additional - get length of palindrome string
    #length_of_palindrome=sum(chr_even+chr_odd)-chr_cnt_odd+(total_single_odd_cnt and 1)

    #print('length of palindrome:', length_of_palindrome)

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






    

