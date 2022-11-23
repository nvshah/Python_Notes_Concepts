def tricky_assignment():
    # Cyclic Reference
    a, b = a[:] = [[]], []
    b.append('b')
    print(a, b)

    print(f'{a is a[0]=}')
    
    '''
        temp = [[]], []
        a, b = temp
        a[:] = temp
    '''

def tricky_q1():
    #sra, b = a[b] = a = [1,2,3], 2
    a, b = b[a] = a = 2, [1,2,3]
    print(a,b)# 2, [1, 2, (...)]) [1, 2, (2, [...])]

tricky_assignment()

tricky_q1()

