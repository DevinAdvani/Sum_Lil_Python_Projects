#Imports
import matplotlib.pyplot as plt
import numpy as np
import math

def QF(a,b,c):#Quadratic formula
    return ((-b+(math.sqrt((b^2)-(4*a*c))))/(2*a))
    return ((-b-(math.sqrt((b^2)-(4*a*c))))/(2*a))



#Inputs
PED, DI, ACX, ACY, ACF, MCX, MCY = float(input("Enter PED (Negative): ")),float(input("Enter Demand Intercept With Y Axis (Positive): ")),float(input("Enter Average Cost Lowest X Coordinate: ")),float(input("Enter Average Cost Lowest Y Coordinate: ")),float(input("Enter Average Cost Flatness (Positive): ")),float(input("Enter Marginal Cost Lowest X Coordinate: ")),float(input("Enter Marginal Cost Lowest Y Coordinate: "))

#Print Important Data
#MR = MC Price, Quantity, Cost, TR, Profit
#Welfare Loss
#Productive Efficiency
#Allocative Efficiency

#Idk what these functions do, I copied the internet
fig= plt.figure()
axes= fig.add_axes([0.1,0.1,0.8,0.8])
x= np.arange(0,100)

#Plotting Demand/AR and MR
axes.plot(x,((PED * x)+ DI),label='Average Revenue') # AR
axes.plot(x,(((PED * 2) * x)+ DI),label='Marginal Revenue') # MR
axes.plot(x,((((x-ACX)/ACF)**2)+ACY),label='Average Cost') # AC
MCF = (ACX - MCX)/(math.sqrt((ACY - MCY))) # bending curve to go through AC lowest point
axes.plot(x,((((x-MCX)/MCF)**2)+MCY),label='Marginal Cost') # MC



#Plotting inbetween lines
#axes.hlines(y=P, xmin=0, xmax=Q, linestyles = '--', colors = 'black')
#axes.vlines(x=Q, ymin=0, ymax=P, linestyles = '--', colors = 'black')

#x and y range
axes.set_xlim([0,(-DI/PED)+1])
axes.set_ylim([0,DI+1])

#Axis Label
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.legend(loc='upper center')

#Showing plot
plt.show()
