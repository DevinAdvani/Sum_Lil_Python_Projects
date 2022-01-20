#Imports
import matplotlib.pyplot as plt
import numpy as np

#Inputs
PED, DI, PES, SI = float(input("Enter PED (Negative): ")),float(input("Enter Demand Intercept With Y Axis (Positive): ")),float(input("Enter PES (Positive): ")),float(input("Enter Supply Intercept With Y Axis (Either): "))

#Calculating Q and P
Q = (SI-DI)/(PED-PES)
P = (PED * Q) + DI

#Printing information
print(f'QUANTITY = {Q} UNITS')
print(f"PRICE = £{P}")
print(f"TOTAL REVENUE = £{P*Q}")

#Idk what these functions do, I copied the internet
fig= plt.figure()
axes= fig.add_axes([0.1,0.1,0.8,0.8])
x= np.arange(0,100)

#Plotting Supply and Demand
axes.plot(x,((PES * x)+ SI), label='Supply')
axes.plot(x,((PED * x)+ DI), label="Demand")

#Plotting Price and Quantity
axes.hlines(y=P, xmin=0, xmax=Q, linestyles = '--', colors = 'black')
axes.vlines(x=Q, ymin=0, ymax=P, linestyles = '--', colors = 'black')

#x and y range
axes.set_xlim([0,(-DI/PED)+1])
axes.set_ylim([0,DI+1])

#Axis Label
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.legend(loc='upper center')

#Showing plot
plt.show()
