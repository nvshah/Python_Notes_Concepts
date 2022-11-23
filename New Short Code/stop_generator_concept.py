# stop_generator_concept.py

# Before Python 3.7 -> You will not get Exception in Output

def sub():
    yield 11
    return  # raises StopIterator exception
    yield 12


def par():
    yield 1
    s = sub()
    yield next(s)
    yield next(s)  # Exception rethrow :- StopIterator
    yield 2


for i in par():
    print(i)
