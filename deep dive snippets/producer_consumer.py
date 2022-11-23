from collections import deque

def produce_elements(dq, n):
    for i in range(1, n):
        dq.appendleft(i)
        if len(dq) == dq.maxlen:
            print('queue full - yielding control')
            yield
        
def consume_elements(dq):
    while True:
        while len(dq) > 0:
            print('processing ', dq.pop())
        print('queue empty - yielding control')
        yield
    
def coordinator():
    dq = deque(maxlen=10)
    producer = produce_elements(dq, 36)
    consumer = consume_elements(dq)
    while True:
        try:
            print('producing...')
            next(producer)  # this will produce n items at once
        except StopIteration:
            # producer finished
            break
        finally:
            print('consuming...')
            next(consumer)  # this will consume n items at once