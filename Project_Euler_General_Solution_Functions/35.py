def PC(a):
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

def C(x):#circulate
    list = []
    for i in range(0,len(str(x))):
        list.append(int(str(x)[i:]+str(x)[:i]))
    return(list)

set = []

for i in range(1,1000001):
    if PC(i):
        print(i)
        set.append(i)
