# string strip

s = 'www.google.com'
print(s.strip('wcom.'))  # google


# Get the Size of Object

s = '1'
i = 1
f = 1.0
print('size of object in memory in bytes')
print(s.__sizeof__(), i.__sizeof__(), f.__sizeof__())