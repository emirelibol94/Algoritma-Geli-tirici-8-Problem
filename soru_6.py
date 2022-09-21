"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def asal_mi(sayi):
    sayac = 2
    if sayi == 1:
        return False
    else:
        while sayac < sayi:
            if sayac * sayac <= sayi:
                if sayi % sayac == 0:
                    return False
            sayac += 1
        else:
            return True

asal_sayisi = 0
sayac_2 = 0
asal_sayi = 0
while asal_sayisi < 10001:
    sayac_2 += 1
    if asal_mi(sayac_2):
        asal_sayisi += 1
        asal_sayi = sayac_2

print(asal_sayi)