"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

sayac = 0
asal_sayilar_toplami = 0
while sayac < 10:   # 2000000 yazılacak uzun sürmekte belki başka bir şey yapılabilir
    sayac += 1
    if asal_mi(sayac):
        asal_sayilar_toplami += sayac
    print(sayac)
print(asal_sayilar_toplami)