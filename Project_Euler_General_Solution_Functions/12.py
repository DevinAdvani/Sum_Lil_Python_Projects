def f(x):
    y = 0
    for i in range(1,x+1):
        y += i
    return y

f(5)

def g(x):
    primes = []
    a = 1
    while len(primes) != x:
        a += 1
        for i in range(2,a):
            if a % i == 0:
                break
                #need to make a prime function
