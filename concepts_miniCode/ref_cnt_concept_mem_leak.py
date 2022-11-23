from re import T

# Case 1

def case1():
    l = [[1,2], [3,4], [5,6]]

    t = l[1]

    del t  

    # though its deleted still there is 1 ref cnt left in List itself
    print(l)  # [[1,2], [3,4], [5,6]]
  
# Case 2
def case2():
    l = [[1,2], [3,4], [5,6]]

    t = l[1]

    del l[1]

    # though its deleted from list there is 1 ref cnt left ie t
    print(t)  # (3,4)

case2()