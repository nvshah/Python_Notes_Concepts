# 1. eval from string 

s1 = '5 * 10'
s2 = str([i for i in range(3)])

print(eval(s1))  # 50
print(eval(s2))  # [0, 1, 2]

# 2. eval from Compiled Code 
code = compile('2 * 30', "<string>", 'eval')  # the code return by compile should be used with `eval`
print(eval(code))

# 3. on the fly variable {z} here
# Even though z isn’t defined in your current global scope, the variable is present in globals with a value of 300
x, y = 100, 200
res = eval("x + y + z", {"x": x, "y": y, "z": 300})
print(res)  # 600

# 4. builtins names automatically available
print(eval("sum([2, 2, 2])", {}))  # here sum is available
print(eval("min([1, 2, 3])", {})) # here min is available

# See how min() definitionn is changed completely with sum()
print(eval("min([1, 2, 3])", {'__builtins__' : {'min': lambda x: sum(x)}}))

#! don't use below statement because it will remove all files in curr directory
# eval("__import__('subprocess').getoutput('rm –rf *')")


# Restricting the eval() space
print(eval("sum([5, 5, 5])", {}, {}))
# Can able to access the built-ins still after restricting the gloabals() & locals()
print(eval("__import__('math').sqrt(25)", {}, {}))
print(eval("__import__('subprocess').getoutput('echo Hello, World')", {}, {}))

# Restricting the builtins
#print(eval("__import__('math').sqrt(25)", {"__builtins__": {}}, {})) # Error  '__import__' is not defined


#* AMAZING (Without Builtin & Currennt Scope get the range() fun evaluated)
# Eval any expression without any builtins module or global or local scope

# LOOPHOLE :- of eval()
# get range(0, 10) without builtinn or curr namespace scope avaialable 
input_str = '''[
    c for c in ().__class__.__base__.__subclasses__()
    if c.__name__ == "range"
][0](10)'''

# Restricting all globals(), locals() (ie current namespace) & builtin-namesapce as well
# So no builtin fun are avaialble for {input_str}
l = list(eval(input_str, {'__builtins__': {}}, {}))
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Restrictig the names for eval() to avoid the above loophole

def eval_expression(inp_str):
    # Step 1 -> define names that are allowed
    allowed_names = {'sum': sum}  # allowed names are part of local-namespace

    # Step 2 -> compile the {inp_str} -> AST (compiled) bytecode object 
    code = compile(inp_str, '<string>', "eval")

    # Step 3 -> check for names violation in inp_str 
    #     In this case, you use an empty dictionary to restrict locals as well.
    for name in code.co_names:
        if name not in allowed_names:
            # Step 4
            raise NameError(f"Use of {name} not allowed !")
    
    # Step 4 -> inp_str doesnt violate any name constraints for eval()
    # here we are restricting the built-in namespace but allwoing only 1 name from local namespace ie sum
    return eval(code, {"__builtins__": {}}, allowed_names)


# eval_expression has no access to built-in scopes except {sum}
print(eval_expression("sum([1, 2, 3])"))  # 6

print(eval_expression("2 + 3"))  # 5

#print(eval_expression("range(1,10)")) # Error Use of range not allowed !

# try to sneak a loop hole 
input_str = '''[
    c for c in ().__class__.__base__.__subclasses__()
    if c.__name__ == "range"
][0](10)'''
print(eval_expression(input_str))  # Still Error Use of __class__ not allowed !