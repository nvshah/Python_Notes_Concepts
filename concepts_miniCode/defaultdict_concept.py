from collections import defaultdict as dd 
from itertools import count

m = dd(int)

b = 'a' in m 
print(b)  # false
c = 'a' in m 
print(c) # false

d = m['a']

e = 'a' in m 
print(e)  # true

def default_dict_incrementer():
    cntr = count()
    incrementer = dd(cntr.__next__)
    return incrementer
