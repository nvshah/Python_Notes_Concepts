class A:
    def f1():
        print('Inside A')

#a = A()
#A.f1()  # When a type A is created then f1 is defined for A under its namespace 

print(dir(A).count('f1'))  # 1 -> Contains a 'f1' as membet in list 