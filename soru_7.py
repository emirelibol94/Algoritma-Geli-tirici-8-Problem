"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

sayac = True
if sayac:
    for a in range(1,1000):
        if sayac:
            for b in range(1,1000):
                if sayac:
                    for c in range(1,1000):
                        if (a * a) + (b * b) == (c * c) and a + b + c == 1000:
                            print("a:",a," ","b:",b," ","c:",c)
                            print(a*b*c)
                            sayac = False