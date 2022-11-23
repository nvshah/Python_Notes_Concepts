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
