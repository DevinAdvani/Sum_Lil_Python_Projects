import matplotlib.pyplot as plt
import math
x = []
y = []
n=100
a = 7
b = 4
for t in range(0,360*n + 1):
    x.append(math.cos(a*t*(1/n)*math.pi*(1/180)))
    y.append(math.cos(b*(((t/n)*(math.pi/180))-(math.pi/10))))
plt.scatter(x, y)
plt.show()

def m(x1,y1,x2,y2):
    g = (y2-y1)/(x2-x1)
    return g

def c(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    h = y1 - (m*x1)
    return h

def d():
    sum = 0
    xic = []#x intersect coordinates
    yic = []#y intersect coordinates
    for e in range(0,360*n):
        for d in range(0,360*n):
            m1 = m(x[e],y[e],x[e+1],y[e+1])
            c1 = c(x[e],y[e],x[e+1],y[e+1])
            m2 = m(x[d],y[d],x[d+1],y[d+1])
            c2 = c(x[d],y[d],x[d+1],y[d+1])
            if m1 == m2:
                xinput = 0
            else:
                xinput = (c2-c1)/(m1-m2)
            if e != d and m1*xinput + c1 == m2*xinput + c2:#add the intersect
                xic.append(xinput)
                yic.append(m1*xinput + c1)
        return xic

print(d())
