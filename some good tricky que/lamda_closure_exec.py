k = 10
# Why this assignment of k = 1 in lamda is not updating the global variable 
f = lambda x: [exec('k = 1'), x][1]

f(14)        # 2
#print(exec('k = 1')) 
print(k)              # 10 

print(globals()['k']) #10

f2 = lambda x: [globals().update(k=20), x][1]  #Works

f2(21)

#globals().update(k=5)

print(k) #20

