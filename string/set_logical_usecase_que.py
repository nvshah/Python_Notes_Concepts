#!/bin/python3

#MUST SEE QUESTION BELOW TO UNDERSTAND THE APPLICATION OF SET CONCEPT IN REALITY usecase
# Que https://www.hackerrank.com/challenges/string-construction/problem

# Complete the stringConstruction function below.
def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)
        print(result)
