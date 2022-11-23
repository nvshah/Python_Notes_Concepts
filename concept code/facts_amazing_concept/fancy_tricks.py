# Concept :- access the base or subclass via basic object itself

print("".__class__.__base__)

print([].__class__.__base__)

print((20).__class__.__base__)

str_base_class = "".__class__.__base__
for sub_class in str_base_class.__subclasses__():
    print(sub_class.__name__)
    break

#-------------------

#* AMAZING
# Eval any expression without any builtins module or global or local scope

input_str = '''[
    c for c in ().__class__.__base__.__subclasses__()
    if c.__name__ == "range"
][0](10)'''

# Restricting all globals(), locals() (ie current namespace) & builtin-namesapce as well
# So no builtin fun are avaialble for {input_str}
l = list(eval(input_str, {'__builtins__': {}}, {}))
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]