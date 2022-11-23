x = 10
def f1():
    #global x
    #x = 20
    x = 20
    def f11():
        y = x + 15   # get value from nearest x i.e in local scope
        print(y)
    f11()  

f1()
print(x)


#2....
y = 10
def f2():
    global y
    y = 20
    def f22():
        nonlocal y   # no binding for nonlocal 'y' found
        z = y + 20
        print(z)
    f22()

f2()
print(y)
    