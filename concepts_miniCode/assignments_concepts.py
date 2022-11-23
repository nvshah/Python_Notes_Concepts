def walrus_assignments_expr():
    # Right to left
    (a := (b := (c := 10)))
    print(a, b, c)

def chained_assignments_stmt():
    a = b = c = 10 
    # t = 10 # temp
    # a = 10
    # b = 10
    # c = t

    print(a, b, c)