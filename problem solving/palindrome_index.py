import itertools as it

def find_index_tobe_removed(s):
    l = len(s)
    m = l//2         # middle index of string
    s1 = s[:m]       # first part of string
    s2 = s[-1:m-1:-1] if l%2==0 else s[-1:m:-1] # 2nd part of string (neglecting middle element)

    deciding_pairs = zip(s1, s2)

    for n,pair in enumerate(deciding_pairs, start=1):
        #print(pair)
        if pair[0] != pair[1]:
            return len(s)-n if pair[0] == s[-n-1] else n-1
            #return i if s[i+1:min(i+3,m)] == s[-(i+1):min(l-(i+3), m)] else l-i-1
    return -1

#Updated & Correct method  - that give index, removing character from which position will result a palindrome string
def find_index_to_remove(s):
    l = len(s)
    m = l//2-1 if l%2 == 0 else l//2
    for i in range(l//2):
        #print(s[i], s[-(i+1)])
        if s[i] != s[-(i+1)]:
            #return (l-i-1 if s[i] == s[-(i+2)] else i)
            #return i if s[i+1:i+3] == s[-(i+1):-(i+3)] else l-i-1
            #print(s[i+1:min(i+3,m)], s[-(i+1):max(-(i+3), -m-1):-1])
            #return i if s[i+1:min(i+3,m)] == s[-(i+1):max(-(i+3), -m-1):-1] else l-i-1
            #print(l)
            #print(s[i+1:min(i+3,m)], s[-(i+1):max(l-(i+3), m):-1])
            return i if s[i+1:min(i+3,m+1)] == s[-(i+1):max(l-(i+3), m):-1] else l-i-1
    return -1

s = input()

while s:
    print(find_index_tobe_removed(s))
    print(find_index_to_remove(s))

    s = input() #input string



