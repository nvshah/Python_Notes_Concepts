#!/bin/python3
from textwrap import wrap

# Complete the marsExploration function below.
def marsExploration(s):
    changed_letters = 0
    w = wrap(s, 3)
    for batch in w:
        if batch[0] != 'S':
            changed_letters += 1
        if batch[1] != 'O':
            changed_letters += 1
        if batch[2] != 'S':
            changed_letters += 1
    
    return changed_letters
    
if __name__ == '__main__':
    s = input()
    print(result)