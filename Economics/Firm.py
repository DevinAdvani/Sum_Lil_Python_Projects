#Imports
import matplotlib.pyplot as plt
import numpy as np
import math

#Inputs
PED, DI, ACX, ACY, ACF, MCX, MCY = float(input("Enter PED (Negative): ")),float(input("Enter Demand Intercept With Y Axis (Positive): ")),float(input("Enter Average Cost Lowest X Coordinate: ")),float(input("Enter Average Cost Lowest Y Coordinate: ")),float(input("Enter Average Cost Flatness (Positive): ")),float(input("Enter Marginal Cost Lowest X Coordinate: ")),float(input("Enter Marginal Cost Lowest Y Coordinate: "))

#Idk what these functions do, I copied the internet
fig= plt.figure()
axes= fig.add_axes([0.1,0.1,0.8,0.8])
x= np.arange(0,100)

#Plotting Demand/AR and MR
axes.plot(x,((PED * x)+ DI))
axes.plot(x,(((PED * 2) * x)+ DI))
axes.plot(x,((((x-ACX)/ACF)**2)+ACY))
MCF = (ACX - MCX)/(math.sqrt((ACY - MCY))) # bending curve to go through AC lowest point
axes.plot(x,((((x-MCX)/MCF)**2)+MCY))



#Plotting inbetween lines
#axes.hlines(y=P, xmin=0, xmax=Q, linestyles = '--', colors = 'black')
#axes.vlines(x=Q, ymin=0, ymax=P, linestyles = '--', colors = 'black')

#x and y range
axes.set_xlim([0,(-DI/PED)+1])
axes.set_ylim([0,DI+1])

#Showing plot
plt.show()
