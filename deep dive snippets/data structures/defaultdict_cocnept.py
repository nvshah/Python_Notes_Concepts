from collections import namedtuple, defaultdict
from datetime import datetime
from functools import wraps

def func_stats_tracker():
    dataMap = defaultdict(lambda : {'count': 0, 'first_called': datetime.utcnow() })
    Stats = namedtuple('Stats', 'decorator data')
    

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            dataMap[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)
        return wrapper 
    
    return Stats(decorator, dataMap)


stats_tracker = func_stats_tracker()

dec = stats_tracker.decorator
stats = stats_tracker.data

@dec
def cntr(i):
    print(i)

print(stats['cntr'])
cntr(1)
print(stats['cntr'])
cntr(2)
print(stats['cntr'])


            
            
