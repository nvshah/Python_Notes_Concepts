from time import perf_counter, sleep 

class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self
    
    def __exit__(self, err_type, err_val, err_tb):
        self.end = perf_counter()
        self.elapsed = self.end - self.start
        return False 

if __name__ == '__main__':
    with Timer() as t:  # required timer obj to get elapsed time
        sleep(1)
    
    print(t.elapsed)  # 1.0046684730000002
 
    