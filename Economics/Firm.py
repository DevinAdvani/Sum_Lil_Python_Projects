#Imports
import matplotlib.pyplot as plt
import numpy as np
import math

def QF(a,b,c):#Quadratic formula
    return ((-b+(math.sqrt((b**2)-(4*a*c))))/(2*a))#, ((-b-(math.sqrt((b**2)-(4*a*c))))/(2*a)) #See if only need one

#Inputs
PED, DI, ACX, ACY, ACF, MCX, MCY = float(input("Enter PED (Negative): ")),float(input("Enter Demand Intercept With Y Axis (Positive): ")),float(input("Enter Average Cost Lowest X Coordinate: ")),float(input("Enter Average Cost Lowest Y Coordinate: ")),float(input("Enter Average Cost Flatness (Positive): ")),float(input("Enter Marginal Cost Lowest X Coordinate: ")),float(input("Enter Marginal Cost Lowest Y Coordinate: "))

#Calculating Important Data
MCF = (ACX - MCX)/(math.sqrt((ACY - MCY))) # bending curve to go through AC lowest point
MRMCX = QF(1,((-2*MCX)-((MCF**2)*PED*2)),((MCX**2)+(MCY*(MCF**2))-(DI*(MCF**2))))#Doing MRMCX intercept
MRMCY = (PED*MRMCX)+DI #MRMCY
MRMCC = ((((MRMCX-ACX)/ACF)**2)+ACY) # MRMC Cost on price Axis
MRMCTC = MRMCC * MRMCX # MRMC total cost
MRMCTR = MRMCX * MRMCY # MRMC Total Revenue
MRMCPR = MRMCTR - MRMCTC # MRMC total Profit

#Print Important Data
print("")
print(f'Profit Maximising Quantity = {round(MRMCX,2)} UNITS')
print(f'Profit Maximising Price = £{round(MRMCY,2)}')
print(f'Profit Maximising Costs = £{round(MRMCC,2)}')
print(f'Profit Maximising Profit Per Unit = £{round(MRMCPR/MRMCX,2)}')
print("")
print(f'Profit Maximising Total Revenue = £{round(MRMCTR,2)}')
print(f'Profit Maximising Total Costs = £{round(MRMCTC,2)}')
print(f'Profit Maximising Total Profit = £{round(MRMCPR,2)}')

#Idk what these functions do, I copied the internet
fig= plt.figure()
axes= fig.add_axes([0.1,0.1,0.8,0.8])
x= np.arange(0,(-DI/PED)+1)

#Plotting Demand/AR and MR
axes.plot(x,((PED * x)+ DI),label='Average Revenue') # AR
axes.plot(x,(((PED * 2) * x)+ DI),label='Marginal Revenue') # MR
axes.plot(x,((((x-ACX)/ACF)**2)+ACY),label='Average Cost') # AC
axes.plot(x,((((x-MCX)/MCF)**2)+MCY),label='Marginal Cost') # MC

#Plotting inbetween lines
axes.hlines(y=MRMCY, xmin=0, xmax=MRMCX, linestyles = '--', colors = 'black')
axes.vlines(x=MRMCX, ymin=0, ymax=MRMCY, linestyles = '--', colors = 'black')#Slightly Off But Fuck It
axes.hlines(y=MRMCC, xmin=0, xmax=MRMCX, linestyles = '--', colors = 'black')


#x and y range
axes.set_xlim([0,(-DI/PED)+1])
axes.set_ylim([0,DI+1])

#Axis Label
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.legend(loc='upper center')

#Showing plot
plt.show()
