'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def f(x):
    primes = []
    y = 1
    while len(primes) != x:
        y += 1
        for i  in range(2,y+1):
            if
