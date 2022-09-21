"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
sayi = 600851475143

def asal_mi(asal):
    if asal == 1:
        return False
    else:
        for i in range(2,asal):
            if asal % i == 0:
                return False
                break
        else:
            return True
asal = 1
en_buyuk_asal = 0
while sayi > 1:
    if asal_mi(asal):
        while sayi % asal == 0:
            sayi /= asal
            if en_buyuk_asal < asal:
                en_buyuk_asal = asal
    asal += 1

print(en_buyuk_asal)
