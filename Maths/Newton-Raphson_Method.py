#This was basically the concept of which root would you calculate depending upon the initial value placed into the calculator with the Newton-Raphson Method

#imports
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#Roots to the equation are

#Function and other inputs
def fun(x):
    return (x - 1)*(x - 2)*(x - 3)*(x - 4)
repeats = 100
lower_bound = 2.37730
upper_bound = 2.37807
step = 0.000001

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
    for i in range(0,repeats):
        x = NRM(x)
    return x

#X and Y values dictionnary
x = []
y = []
N = lower_bound
while N < upper_bound:
    x.append(N)
    N += step
N = lower_bound
while N < upper_bound:
    y.append(RNRM(N))
    N += step

#Sketch
plt.plot(x,y)
plt.show()
