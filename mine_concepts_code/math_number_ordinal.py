def ordinal(n): return "%d%s" % (
    n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])


print(ordinal(1))

# ----------------


def round_cncept():
    n = 29232675
    print(round(n, -1))
    print(round(n, -2))
    print(round(n, -3))


round_cncept()
