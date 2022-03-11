#imports
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#Function
def fun(x):
    return x**2 - 2

#Derivative
def d_fun(x):
    h = 1e-5
    return (fun(x+h)-fun(x-h))/(2*h)

#Newton-Raphson Method
def NRM(x):
    x = x - (fun(x)/d_fun(x)) if d_fun(x) != 0 else 0
    return x

#Repeated Newton-Raphson Method
def RNRM(x):
    for i in range(0,100):
        x = NRM(x)
    return x

#X and Y values dictionnary
x = []
for i in range(-100,100):
    x.append(i)
y = []
for i in range(-100,100):
    y.append(RNRM(i))
#Sketch
plt.plot(x,y)
plt.show()
