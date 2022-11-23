from numbers import Number

# predicate
def is_a_num(o):
    return isinstance(o, Number)

l = [1, '1', 2, 0, 'Haha']
pred_l = [is_a_num(e) for e in l]

print(all(pred_l)) # False


# 2 generator and pred

g = (i for i in range(5))
print(any(e > 1 for e in g))  # True
print(*g)  # 3 4