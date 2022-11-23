def gen():
    try:
        print('Start')
        yield 2
        print('Stop')
    except GeneratorExit:
        print("gen exit")
        raise

g = gen()
print(next(g))
#print(next(g))  # stopIteration
g.close()