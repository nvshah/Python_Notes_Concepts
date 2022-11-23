def f(): print('hello Man')
#function as arg of print as other ordinary objects like string or num
print("Olah", f, "Uhhh") #Olah <function f at 0x10a9461e0> Uhhh

#function as member in list
o = [1, "1", f, (1,2,3)]

# function as key in dictionary
d = {"c": 1, f: 2, 3:3 }

o[2]()  # hello man
print(d[f]) # 2


#-----------

#-> function to other function

def f1(): print('From f1()')

def f2(f): f()

f2(f1)


#------------

#-> callable check

callable(lambda: print('dsds'))

#-------------- LAMBDA

# returning the tuple from lambda vs from function

def f(): return 1,2,3,4

l2 = lambda: (1,2,3,4)  #Here explicitly parenthesis is required to tell that returning is tuple

f()
l2()

print("Hello {lambda : 'Peter'}")  # Error as parenthesisi is not used 
#lambda inside f string requires ()
print("Hello {(lambda : 'Peter')}")
