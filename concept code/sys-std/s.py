import sys

sys.stdin = open("ip.txt", 'r')
sys.stdout = open("op.txt", "w")

# As input() uses underneath the sys.stdin.read() to read inputs from stream
i = input()  # Takes input from ip.txt file
# print() defaults to stdout -> for displaying on console
print(i)