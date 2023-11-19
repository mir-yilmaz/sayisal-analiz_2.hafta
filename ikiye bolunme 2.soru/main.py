
#ikiye bolunme 2. soru

def f(x):
    return  x**3 + 4*x**2 - 10 #fonksiyonu tanımladık

a = 1  #hangi iki değer arasıdan olacağini belirtim
b = 2


def ikiye_bolme(a, b,max_iter): #değişkenleri tanımladım

    iterasyon = 0  #0 incı iterosayndan başlayıp 4 e kadar devam edecek

    while  iterasyon < max_iter: #kok hata payından kucuk oluncaya kadar devam edecek
        c = (a + b) / 2

        if f(c) == 0:

            print("bu iki kok arasında kök bulunmuyor")
            break
        elif f(c) * f(a) < 0:# c negatif değer alırsa yeni aralik c ile a arasında olur
            b = c
        else:
            a = c  #değilse b ile c arasında olur

        iterasyon += 1

    return (a + b) / 2

max_iterasyon = 4

kok = ikiye_bolme(a, b,max_iterasyon)

print(f"Denklemin kökü: {kok}")