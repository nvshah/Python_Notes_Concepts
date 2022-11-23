import json

t = (1, 2, 3)
t_e = json.dumps(t)  # encoded json array
l = json.loads(t_e)

print(t)  # (1,2,4)
print(l)  # [1,2,3]

"""
NOTE : object before encoding : tuple
       object after decoding  : list

       So it's not always necessary that you will get exact same object what you encode, while decoding
"""

print(type(t))  # <class 'tuple'>
print(type(l))  # <class 'list'>
