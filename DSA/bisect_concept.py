import bisect

l = [1,2,3,3,4,5,5,6]

i1 = bisect.bisect_left(l, 3)  # 2
i2 = bisect.bisect(l, 3)       # 4
i3 = bisect.bisect_right(l, 3) # 4

print(i1, i2, i3)