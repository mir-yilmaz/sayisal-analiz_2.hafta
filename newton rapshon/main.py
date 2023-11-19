import math

def f(x):
    return 4 * math.exp(-0.5 * x) - x

def f_turev(x):
    return -2 * math.exp(-0.5 * x) - 1

def newton(x0, iterasyon):
    for i in range(iterasyon):
        x0 = x0 - f(x0) / f_turev(x0)
        print(f"{i + 1}. iterasyondaki kök: {x0}")
    return x0


x0 = 2
iterasyon = 4

print("kök:", newton(x0, iterasyon))
