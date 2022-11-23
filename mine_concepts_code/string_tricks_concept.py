s = "dsdsds"
print(s.strip('ds'))  # empty string 

'''
Thus strip() will recursively remove leading & trailing character till found
'''

s = "dfsghrtsndfdf"
print(s.strip('df'))  # sghrtsn


# -----------
# FOrmated String

s1 = f'{10:#>10}'  # ########10
s2 = f'{10:_<10}'  # 10________
s3 = f'{10:*^10}'  # ****10****
print(s1)
print(s2)
print(s3)
