def PC(a):
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

primes = [2]
n = 3
while primes[-1] < 1000000:
    if PC(n):
        primes.append(n)
    n += 2
    print(n)
print(primes)
