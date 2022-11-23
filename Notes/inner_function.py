#CLosure that can modify its enclosing state
def mean():
    sample = []
    def inner_mean(n):
        sample.append(n)
        return (float(sum(sample)) / len(sample))
    return inner_mean

mean_calc = mean()

v1 = mean_calc(1)
v2 = mean_calc(2)
v3 = mean_calc(6)

print(v1, v2, v3)  #Cumulutaive means : 1, 1.5, 3