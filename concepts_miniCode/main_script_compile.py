def f():
    print('HAhA')

# __main__ is current module name in namespace
e = compile('from __main__ import f as f2', filename='sample', mode='exec')
exec(e)
f2()

from __main__ import f2 as f22

f22()