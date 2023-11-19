import math


def f(x):
    return (4 * math.exp(-0.5 * x)) - x

def f_turev(x):
    return (-2 * math.exp(-0.5 * x)) - 1

def newton(x0, iterasyon):
    for i in range(iterasyon):
        x1 = x0 - f(x0) / f_turev(x0)
        x0 = x1
    return x1

x0 = 2
iterasyon = 4
kok = newton(x0, iterasyon)
print("Kök: ",kok)
