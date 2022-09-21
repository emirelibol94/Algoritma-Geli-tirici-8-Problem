"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

kareler_toplami = 0
toplamin_karesinin_toplami = 0

def kareler_toplami(sayi):
    kareler_toplami = sayi * (sayi + 1) * ((2 * sayi) + 1) / 6
    return kareler_toplami

for j in range(101):
    toplamin_karesinin_toplami += j
toplamin_karesinin_toplami *= toplamin_karesinin_toplami

print(toplamin_karesinin_toplami - kareler_toplami(100))