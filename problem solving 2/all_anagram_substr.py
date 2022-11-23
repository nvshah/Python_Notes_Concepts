from collections import Counter as ctr
import itertools as it
import functools as ft
import operator as op

#List Equality Ignoring Order 
#Compare List despite ignoring elements order
#comparing cnt & value of elements between both list
def checkListEqualityIgnoringOrder(l1, l2):
    l1_ctr = ctr(l1)
    l2_ctr = ctr(l2)
    for k in l1_ctr:
        if l1_ctr[k] != l2_ctr[k]:
            return False
    return True
    #l1_ctr.subtract(l2_ctr)
    #return not(any(l1_ctr.values()))

# def checkListEqualityIgnoringOrder(l1, l2):
#     l1_ctr = ctr(l1)
#     l2_ctr = ctr(l2)
#     for k in l1_ctr:
#         if l1_ctr[k] != l2_ctr[k]:
#             return False
#     return True

@ft.lru_cache()
def fact(n):
    if n == 0:
        return 1
    if n<3:
        return n
    return ft.reduce(op.mul, range(2,n),1)

def multiplyAll(l):
    if l:
        return ft.reduce(op.mul, l, 1)
    return 1

@ft.lru_cache()
def nCr(n,r):
    #NOTE: when we do nC2 then it will always give us integer number 
    return multiplyAll(range(n,max(n-r,r),-1)) // fact(min(n-r,r))

def findAllAnagramSubstrPair(s):
    total_cnt = 0
    length = len(s)
    for step in range(1, length):
        substrs = [s[i:i+step] for i in range(0,length+1-step)]
        #print(substrs)
        substr_ctr = ctr(substrs)
        #print(substr_ctr)
        for count in filter(lambda cnt: cnt>1, substr_ctr.values()):
            total_cnt += nCr(count,2)
        for pair in it.combinations(substr_ctr.keys(), 2):
            #print(pair)
            if isAnagram(pair[0], pair[1]):
                total_cnt += substr_ctr[pair[0]] * substr_ctr[pair[1]]

    return total_cnt




#l1 = [1,2,3,3,1]
#l2 = [2,3,1,1,3]

#print(compareListDespiteOrder(l1,l2))

c = findAllAnagramSubstrPair('gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde')

print(c)
    