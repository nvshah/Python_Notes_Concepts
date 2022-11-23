import datetime
import calendar
import random
import math
import os

# 1 rads & degree
print(math.sin(math.radians(90)))  # sin(90)

# 2 Todays date
print(datetime.date.today())

# 3 leap year
print(calendar.isleap(2020))

# 4 random pick
print(random.choice([1, 2, 3, 4, 5]))

# 5 current directory
print(os.getcwd())

# 6 bit length of an int
print((11).bit_length())

# ---------------

# 6 to get path of standard library just get path og any module living in that standard library directory/folder
# let say one such module `os`
print(os.__file__)  # path where os module belongs on system
"""
i.e we know `os` module  is part of standard library that comes as battery included in python
    So the directory in above path will be path to standard library where many such modules resides.
"""
