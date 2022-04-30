def f(x):
    sum = 0
    for i in range(0,len(str(x))):
        sum += (int(str(x)[i:i+1]))**2
    return sum

def g(n):
    while True:
        n = f(n)
        if n == 1 or n == 89:
            break
    if n == 89:
        return True
    else:
        return False

num = 0
for i in range(1,10000000):
    print(i)
    if g(i):
        num += 1

print(num)

#create a list of numbers instead that go to 89 if touched, massive list should be more efficient
