#Imports
import matplotlib.pyplot as plt
import numpy as np

'''
#Inputs
PED, PES, DI, SI = float(input("Enter PED (Negative): ")),float(input("Enter PES (Positive): ")),float(input("Enter Demand Intercept With Y Axis (Positive): ")),float(input("Enter Supply Intercept With Y Axis (Either): "))

#Calculating Q and P
Q = (SI-DI)/(PED-PES)
P = (PED * Q) + DI

#Printing information
print(f'QUANTITY = {Q} UNITS')
print(f"PRICE = £{P}")
print(f"TOTAL REVENUE = £{P*Q}")

'''
#plotting graphs
x = np.linspace(0,10,10) # second and third variable should depend on graph size - plots graph size
y = 2*x+1
plt.plot(x, y, '-r', label='y=2x+1')
plt.title('Graph of y=2x+1')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
