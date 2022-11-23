from functools import lru_cache

def memoizer_kwargs(fn):
    ''' Order of KeyWord arguments doesn't matters
        Order of Positional Arguments does matters
    '''
    cache = {} 

    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key not in cache:
            res = fn(*args, **kwargs)
            cache[key] = res 
        return cache[key]

    return inner

def memoizer_all(fn):
    ''' Order of any argument doesn't matter unless all passed argumennts are same
        Imp using frozenset
    '''
    cache = {} 

    def inner(*args, **kwargs):
        key = frozenset(args) | frozenset(kwargs.items())
        if key not in cache:
            res = fn(*args, **kwargs)
            cache[key] = res 
        return cache[key]

    return inner


@lru_cache
def my_func1(*, a, b):
    print('func1 calc a + b ...')
    return a + b 

@memoizer_kwargs
def my_func2(*, a, b):
    print('func2 calc a + b ...')
    return a + b

@memoizer_all
def my_func3(a, b, c,/,d,e):
    print('func3 calc a + b + c + d + e...')
    return a + b + c + d + e


my_func1(a=1, b=2)  # new calc
my_func1(a=1, b=2)
my_func1(b=2, a=1)  # new calc
my_func1(b=2, a=1)

my_func2(a=1, b=2)  # new calc
my_func2(a=1, b=2)
my_func2(b=2, a=1)
my_func2(b=2, a=1)

my_func3(1,2,3,d=10, e=20)  # call 
my_func3(3,2,1,e=20, d=10)


