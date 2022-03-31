primes = []

for i in range(2,2001):
    primes.append(i)

for a in primes:
    for b in primes:
        print(a,b)
        if b % a == 0:
            primes.remove(b)

print(sum(primes))
