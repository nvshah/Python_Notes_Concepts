import itertools as it

def skip(l, skip=0):
    i = 0
    while(i != skip):
        i += 1
    while i < len(l):
        yield l[i]
        i += 1

def takewhile(l, p):
    ''' return grp of elems that satisfy the predicate for entire seq {l} '''
    t = iter(l) # traverser
    while True:
        *s, = it.takewhile(p, t)
        if not s:
            return 
        yield s

def inp1():

    l = [1,2,3,4,5,6]
    #rpl2 = list(skip(l, 2))
    print(list(skip(l, 2)))  # [3,4,5,6]
    print('Over')

def inp2():
    s = '123#456#789'
    p = lambda x: x!='#'
    itr = takewhile(s, p)
    for g in itr:
        print(g)

if __name__ == '__main__':
    inp2()