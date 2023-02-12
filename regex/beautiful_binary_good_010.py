import re

#regex - replaces 010 to 011 when immediate follower(4th element) is 1  i.e (0111)
#        or           to 000 when immediate follower(4th element) is 0 or nothing  i.e (0100, 010)    
regex = r"""
	  010(?=1)(?=.*(011))
	  |
	  010(?=0?)(?=.*(000))
	"""

inp_str = input('Enter binary string : ')
test_str = inp_str + "\n" + "011 000"

subst = "\\1\\2"

flag = re.DOTALL | re.VERBOSE | re.M

# You can manually specify the number of replacements by changing the 4th argument
_, cnt = re.subn(regex, subst, test_str, flags= flag)

print(cnt)

