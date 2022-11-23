import operator as op

l = [1,2,3,4,5]

s1, s2, s3, s4 = l[:2], l[2:], set(l[:2]), set(l[2:])

print(s1)
print(s2)
print(s3)
print(s4)

#Useful when keys are changing but value (i.e 0) remains same
d = {}.fromkeys([1,2,3], 0)  

print(d)   


#zip
        
def f(r,c):
    print(r,c)

z = [*map(f, *zip(*((r,c) for r in range(1, 3+1) for c in range(1, 4+1))))]
print(z)


# Find the small or big element index

l = [4,5,2,8,9,1,7,0]
b = max(range(len(l)), key=l.__getitem__)
s = min(range(len(l)), key=l.__getitem__)

b2 = min(range(len(l)), key=lambda x: op.methodcaller('__getitem__', x)(l))
b1 = max(range(len(l)), key=lambda x: op.methodcaller('__getitem__', x)(l))

print(b2, b1)  # 7 4

print('max idx-> ', b, ' min idx-> ', s)  # max idx->  4  min idx->  7