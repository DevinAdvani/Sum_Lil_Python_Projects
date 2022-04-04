'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def PF(x):
    factors = []
    a = 2
    while x != 1:
        if x % a == 0:
            factors.append(a)
            x = x/a
        else:
            a += 1
    return factors

l = []

for a in range(2,21):
    l.append(PF(a))

print(l)
