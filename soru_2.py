"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
onceki_fibonacci = 0
a = 1
fibonacci = 2
toplam = 0
while fibonacci < 4000000:
    if fibonacci % 2 == 0:
        toplam += fibonacci  
    onceki_fibonacci = fibonacci 
    fibonacci += a
    a = onceki_fibonacci
print(toplam)