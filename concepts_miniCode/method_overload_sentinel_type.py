from typing import overload, List 

SENTINEL = object()

@overload      # Just use for Static Type Checking
def f2(a: int):       
    print('int, ', a)

def f2(a = SENTINEL):
    if a is SENTINEL:
        raise 'kjsdjs'
    else:
        print('sds')

f2(10)