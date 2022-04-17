def f(x):
    return round(x**(1/len(str(x))),14)

sum = 0
n = 0
while True:
    n += 1
    if f(n) == int(f(n)):
        sum += 1
        print(n)
    #print(sum)

#need to reverse engineer it for integer to a certain power
