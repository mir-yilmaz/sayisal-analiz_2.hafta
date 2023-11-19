
# ikiye bolme 1.soru


def f(x):
    return x ** 3 - 2 * x ** 2 - 5 # fonksiyonu tanımladım

# hangi iki deger arasında olacagini yazdım
a = 2
b = 4

def ikiye_bolme_metodu(a, b, max_iterasyon):
    iterasyon = 0
    while iterasyon < max_iterasyon:   #4 isterasyon olana kadar dongu devam edecek
        c = (a + b) / 2# ikiye bolme metodu formulu


        if f(c)== 0:
            return c
        elif f(a) * f(c) < 0:
            b = c # f(c) negatifse kokler a ve c arssında olur
        else:
            a = c ## f(c) pozitifse  kokler b ve c arssında olur

        iterasyon += 1

    return (a + b) / 2


# Maks iterasyon sayısı
max_iterasyon = 4

kok = ikiye_bolme_metodu(a, b, max_iterasyon)

print("Bulunan kök:", kok)
