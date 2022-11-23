from dis import dis


def f1(x):
    return x * 1 // 2  # better


def f2(x):
    return x * (1 // 2)  # compact but req more instr


print("start")
print(dis(f1))  # underhood less instructions are required hence fast i.e # 5 instr

print(dis(f2))  # underhood more instructions are required hence slow i.e # 9 instr
print("end")
