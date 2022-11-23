from collections import Counter as ctr
import itertools as it

def list_intersection(l1, l2):
    l1_ctr = ctr(l1)
    l2_ctr = ctr(l2)
    
    l1_set, l2_set = set(l1), set(l2)
    common_members = l1_set.intersection(l2_set)
    
    if not common_members:
        return []
    
    ans = []
    
    for m in common_members:
        ans.extend(it.repeat(m, min(l1_ctr[m], l2_ctr[m])))

    return ans  

print(list_intersection('dsds dsds sds sd'.split(), 'dsd ss'.split()))
    
    
    
    
        
        