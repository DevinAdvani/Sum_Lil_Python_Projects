def f(x1,y1,x2,y2,x3,y3):#1 to 2
    m = (y2-y1)/(x2-x1)
    c = y1 - (m * x1)
    if m*x3 + c > y3:
        if c > 0:
            return True
        else:
            return False
    else:
        if c < 0:
            return True
        else:
            return False

def g(a1,b1,a2,b2,a3,b3):#for each combination
    if f(a1,b1,a2,b2,a3,b3):
        if f(a2,b2,a3,b3,a1,b1):
            if f(a3,b3,a1,b1,a2,b2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def h(z):
    y = z.split(",")
    return y

f = open('102.txt','r')

count = 0

for x in f:
    a,b,c,d,e,f = (int(h(x[:-1])[0]),int(h(x[:-1])[1]),int(h(x[:-1])[2]),int(h(x[:-1])[3]),int(h(x[:-1])[4]),int(h(x[:-1])[5]))
    print(callable(f(1,2,3,4,5,6)))


print(count)
