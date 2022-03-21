'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def f(x):#where x is the highest number
    list = []
    if x % 2 == 0:
        for i in range(int(x/2 + 1), x+1):
            list.append(i)
    if x % 2 == 1:
        for i in range(round(x/2)+1,x+1):
            list.append(i)
    print(list)
    primes = []
    z = 0
    for i in range(2,x):
        for j in range(0,len(primes)+1):


print(f(37))

#need to divide list element into prime factors and then find lowest common multiple
#find prime numbers
