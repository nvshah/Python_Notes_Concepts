from collections import Counter as ctr

from sqlalchemy import over


def add_subtract_ctr():
    s1 = 'abcdbd'
    s2 = 'dfksns'
    print(ctr(s1) + ctr(s2))

    print(ctr(s1) - ctr(s2))

    overall = ctr(s1) + ctr(s2)
    print(overall.most_common(1)[0][1])

def init_ctr():
    s = 'ballon'
    s2 = 'laebolko'
    c1 = ctr(b=0, a=0, l=0, o=0, n=0)
    #c2 = ctr.fromkeys(set(s), 0)

    c3 = ctr(s2)

    #print(c1 == c2)
    print(c1)
    print(c3)

    al = c1 + c3 
    print(al['n'])

    for k in c3:
        print(k)

init_ctr()
