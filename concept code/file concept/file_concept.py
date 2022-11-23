# 1
f = open('sample.txt')
print(f.name, f.mode)
f.close()

# 2
with open('sample.txt') as f:
    pass 
print(f.closed)  # still f can be accsessible but file is closed

# 3 read in chunks
with open('sample.txt') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while f_contents:
        print(f_contents, end='-')
        f_contents = f.read(size_to_read)

# 4 seek & tell 
with open('sample.txt') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())
    print(f_contents, end='')
    f.seek(0)
    print(f.read(size_to_read))

# 5 Amazing Overwrite Concept
with open('teste.txt', 'w') as f:
    f.write('test')
    f.seek(0)
    f.write('w')  # west in teste.txt
    