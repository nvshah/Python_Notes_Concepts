import numpy as np
from timeit import timeit

def while_loop(n=1000_000_000):
    i = s = 0
    while i < n:
        s += i
        i += 1
    return s

def for_loop(n=1000_000_000):
    s = 0
    for i in range(n):
        s += i
    return s

def for_loop_comprehension(n=1000_000_000):
    return sum([i for i in range(n)])

def builtin_loop(n=1000_000_000):
    return sum(range(n))

def numpy_loop(n=1000_000_000):
    return np.sum(np.arange(n))

def sum_using_formula(n=1000_000_000):
    return (n * (n-1))/2

if __name__ == '__main__':
    print("while loop ", timeit(while_loop, number=1))
    print("foor loop ", timeit(for_loop, number=1))
    print("for loop comprehension ", timeit(for_loop_comprehension, number=1))
    print("sum builtin ", timeit(builtin_loop, number=1))
    print("numpy loop ", timeit(numpy_loop, number=1))
    print("Formula ", timeit(sum_using_formula, number=1))