import math

def PC(a):
    b = 0
    for i in range (2,round(math.sqrt(a))+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

N = 1000000000000

while True:
    N += 1
    if PC(N) == True:
        print(N)
