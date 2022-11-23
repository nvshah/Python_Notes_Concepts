import functools
import time

#? Note here !r specifier means that repr() is used to represent the value respectively 

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):  
        sum([i**2 for i in range(10000)])

print(waste_some_time.__name__)  #  waste_some_time  because we have wrapper_timers