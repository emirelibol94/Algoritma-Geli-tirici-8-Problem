"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
carpim = 0
en_buyuk_carpim = 0
for i in range(999):
    for j in range(999):
        carpim = i * j
        carpim = str(carpim)
        if carpim == carpim[::-1]:
            carpim = int(carpim)
            if en_buyuk_carpim < carpim:
                en_buyuk_carpim = carpim
print(en_buyuk_carpim)