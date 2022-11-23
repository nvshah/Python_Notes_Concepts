from collections import defaultdict as dd 

m = dd(int)

b = 'a' in m 
print(b)  # false
c = 'a' in m 
print(c) # false

d = m['a']

e = 'a' in m 
print(e)  # true