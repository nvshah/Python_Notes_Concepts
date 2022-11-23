def averager():
    total = 0
    cnt = 0
    def inner(n):
        nonlocal total, cnt
        total += n 
        cnt += 1
        return total / cnt
    return inner 

def running_averager():
    total = 0
    cnt = 0
    curr_avg_val = None 
    while True:
        num = yield curr_avg_val
        total += num 
        cnt += 1
        curr_avg_val = total / cnt

def running_averages(l):
    ra = running_averager()
    next(ra)  # to skip None
    for n in l:
        avg = ra.send(n)  # sending n to get curr avg val for n
        print(avg)


avg = averager()
l = [1,2,3,4,5]
# for n in l:
#     print(avg(n))

running_averages(l)
