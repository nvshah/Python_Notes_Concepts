# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

a, b = (1, 3)

print(a, b)
m = {1:1, 2:2}
m2 = dict(map(lambda k: (k[0], str(k[1])), m.items()))
m3 = {*map(lambda k: (k[0], str(k[1])), m.items())}
print(m)
print(m2)
print(m3)
print(dict(m3))