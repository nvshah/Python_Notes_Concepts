import sys 
import cProfile

def g():
    i = 0
    while True:
        i+=1
        print('increment')
        yield i

k = g()

print('started')

# for i in range(3):
#    print(next(k))
#-------------------------

# 1) size test

nums_squared_lc = [i * 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))  # 87616

nums_squared_lc = (i * 2 for i in range(10000))
print(sys.getsizeof(nums_squared_lc))  # 112


# 2) Time test

print(cProfile.run('sum([i * 2 for i in range(10000)])'))
print(cProfile.run('sum((i * 2 for i in range(10000)))'))
