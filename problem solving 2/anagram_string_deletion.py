s1 = input('enter string 1:')
s2 = input('enter string 2:')

print(len(s1), len(s2))

s1_set,s2_set = set(s1), set(s2)

common = s1_set.intersection(s2_set)

# Approach 1------------------------------
print(common)

s1_common_cnt = sum([s1.count(n) for n in common])
s2_common_cnt = sum([s2.count(n) for n in common])

common_removal_cnt = sum([abs(s1.count(n) - s2.count(n)) for n in common])

print(s1_common_cnt, s2_common_cnt)

s1_removal_cnt = len(s1) - s1_common_cnt
s2_removal_cnt = len(s2) - s2_common_cnt

print(s1_removal_cnt,s2_removal_cnt)

print(s1_removal_cnt + s2_removal_cnt + common_removal_cnt)


#Approach2------------------------------

common_cnts = [(s1.count(n), s2.count(n), abs(s1.count(n) - s2.count(n))) for n in common]

[sum(s1_common_cnt), sum(s2_common_cnt), sum(common_removal_cnt) for  in zip(*common_cnts)]


common_removal_cnt= []



