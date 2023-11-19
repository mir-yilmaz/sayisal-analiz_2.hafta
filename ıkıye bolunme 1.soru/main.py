
# ikiye bolme 1.soru


def f(x):
    return  x ** 3 - 2 * x ** 2 - 5

a, b = 2, 4
max_iter = 4

for iterasyon in range(1, max_iter + 1):
    c = (a + b) / 2
    if f(c) == 0:
        print("bu iki nokta arasında kök bulunmuyo!")
        break
    elif f(c) * f(a) < 0:
        b = c
    else:
        a = c

    print(f"{iterasyon}. iterasyondaki kök: {c}")

kok = (a + b) / 2
print(f"kök: {kok}")
