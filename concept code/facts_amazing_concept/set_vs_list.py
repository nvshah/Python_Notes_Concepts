from timeit import timeit

N = 100_000

s = {i for i in range(N)}
l = [i for i in range(N)]

# TIME ---------

no = 100
#search = 5000
search = -1 # Worst case
t_list = timeit(f'{search} in l', globals=globals(), number=no)
t_set = timeit(f'{search} in s', globals=globals(), number=no)

print(t_list)  # 0.11 s
print(t_set)   # 7e-6 s

# SPACE ----------

print(f'size : {s.__sizeof__()=} bytes')  # 4194504 bytes
print(f'size : {l.__sizeof__()=} bytes')  # 824440  bytes