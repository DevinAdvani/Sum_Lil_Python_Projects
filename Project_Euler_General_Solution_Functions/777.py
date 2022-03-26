import matplotlib.pyplot as plt
import math
x = []
y = []
n=100
a = 7
b = 4
for t in range(0,360*n + 1):
    x.append(round(math.cos(a*((t/n)*math.pi/180)),7))
    y.append(round(math.cos(b*(((t/n)*math.pi/180)-(pi/10))),7))
plt.scatter(x, y)
plt.show()

def m(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    c = y1 - m*x1
    return m

def m(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    c = y1 - m*x1
    return c


def d(a,b):
    sum = 0
    a = []
    b = []
    for c in range(0,360*n + 1):
        for d in range(0,360*n + 1):
            print(c,d)
            if c != d and x[c] == x[d] and y[c] == y[d]:
                a.append(x[c])
                b.append(y[c])
    for i in range(0,len(a)):
        sum += (a[i]**2 + b[i]**2)
        return sum
