from collections import Counter as ctr
import itertools as it

# returns list of index that needs to be altered inorder to make string palindrome 
def find_indexes_to_be_altered(s):
    l = len(s)
    return {i for i in range(l//2) if s[i] != s[-(i+1)]}

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    l = len(s)
    #if string contains only 1 character then just check if it's max or not, if allowed alteration, & return likewisew
    if l == 1:
        if k:
            return '9'
        else:
            return s

    #get list of characters of string
    str_chrs = list(s)  
    #list of indices that need to be altered inorder to make string palindrome
    idx_req_altered = find_indexes_to_be_altered(s)
    #total no. of characters that need to be altered inorder to make string palindrome
    req_alter = len(idx_req_altered)
    
    #no. of alterations cannot suffice required alterations i.e 
    #with given allowed alterations we cannot make string palindrome
    if req_alter and req_alter > k:
        return '-1'
    
    #Make string palindrome first
    for idx in idx_req_altered:
        str_chrs[idx] = str_chrs[-(idx+1)] = str(max(int(s[idx]), int(s[-(idx+1)])))
    
    #left alteration permission
    extra_alterations = k - req_alter
    
    #if we have left with alterations then we will try to maximise palindrome number 
    if extra_alterations:
        m = l//2-1 if l%2 == 0 else l//2 #middle index
        for idx in it.filterfalse(lambda i: str_chrs[i] == '9', range(l//2)):
            if idx in idx_req_altered:
                str_chrs[idx] = str_chrs[-(idx+1)] = '9' #step towards maximising palindrome
                #As this character already used earlier 1 alterations so only 1 alteration is req. for it's partner
                extra_alterations -= 1 
            elif extra_alterations > 1:  
                str_chrs[idx] = str_chrs[-(idx+1)] = '9'  #step towards maximising palindrome
                extra_alterations -= 2 #used 2 extra alterations 
            if not extra_alterations: #no alterations are left, thus no. is maximised
                break
        else: #we still have extra alterations left & 
            if l%2 != 0:       #there is unique middle element i.e single without pair so maximise it
                str_chrs[m] = '9'

    return ''.join(str_chrs)


if __name__ == '__main__':
    
    #len, no_of_repeatation_allowed
    n, k = map(int, input('Enter n, k: ').split())
    s = input('Enter string: ')
    
    while s != 'e':

        hvp = highest_value_palindrome(s, k)
        print(hvp)
        
        n, k = map(int, input('Enter n, k: ').split())
        s = input('Enter string: ')

    #s_ctr = ctr(s)
    #get digits whose counts are in odd number
    #digit_with_odd_cnts = s_ctr

    #First check if string can be made palindrom