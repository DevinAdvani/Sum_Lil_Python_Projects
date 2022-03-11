#imports
import numpy as np
import matplotlib.pyplot as plt

#equation, range and step
equation = input("EQUATION: ")
first = input("FIRST NUMBER: ")
final = input("FINAL NUMBER: ")
step = input("STEP: ")

#sketch equation
x = np.linspace(-100, 100, 100)
y = eval(equation)
fig = plt.figure(figsize = (10, 5))
plt.plot(x, y)
plt.show()

#differentiate and repeat and produce
#sketch graphs

x = 1


equation = ('x**2')

for i in range(0,100):
    x += 1
    e = eval(equation)
    print(e)
