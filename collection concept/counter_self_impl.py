def counter(nums):
    ctr = {}
    for e in nums:
        ctr[e] = 1 + ctr.get(e, 0)
    return ctr
