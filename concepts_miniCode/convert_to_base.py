
from math import ceil


def decimalToBase(n, b):
    '''
        Convert decimal num {n} to base {b}
    '''
    if n == 0: return "0"
    res = []
    if b < 0:
        while n:
            n, r = ceil(n/b), abs(n%b)
            res.append(str(r))
    else:
        while n:
            n, r = divmod(n, b)
            res.append(str(r))
    return ''.join(reversed(res))

if __name__ == '__main__':
    n = 6
    ans = decimalToBase(n, 2)
    print(ans)  # 110
    ans = decimalToBase(n, -2)
    print(ans)  # 11010

