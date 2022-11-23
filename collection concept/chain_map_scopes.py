import builtins
from collections import ChainMap

'''
global variable called input 
that shadows the built-in input() function in the builtins scope
'''

input = 42 

pylookup = ChainMap(locals(), globals(), vars(builtins))

# Retrieve input from the global namespace
print(pylookup['input'])  # 42

# Remove input from the global namespace
del globals()['input']

# Retrieve input from the builtins namespace
print(pylookup['input']) # <built-in function input>