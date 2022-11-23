s1 = {1,2,3}
s2 = {2,3}
s3 = {1,4}

s1 -= s2-s3   # s1 - (s2-s3)

print(s1)

s1 = {1,2,3}
s2 = {2,3}
s3 = {1,4}

s1.difference_update(s2, s3)  # (s1-s2)-s3
print(s1)