import sys

# 1. -> exit() like in terminal or interpreter
def f1():
    sys.exit(0)


def f2():
    print("JJJJJ")


if __name__ == "__main__":
    print("Hi before exit")
    f1()
    print("After Exit")  # Unreachable Code


# 2. -> get info about Exception/Error

try:
    a = 1/0
except:
    print('Error ',sys.exc_info()[0], ' Happens !')


