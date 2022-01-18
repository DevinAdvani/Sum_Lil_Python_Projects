#Imports
import matplotlib.pyplot as plt
import numpy as np

#Inputs
PED, DI, PES, SI ,G= float(input("Enter PED (Negative): ")),float(input("Enter Demand Intercept With Y Axis (Positive): ")),float(input("Enter PES (Positive): ")),float(input("Enter Supply Intercept With Y Axis (Positive): ")),float(input("Enter Specific Tax (Positive) or Subsidy (Negative): "))

#Calculating Q and P
Q = (SI-DI)/(PED-PES)
P = (PED * Q) + DI

#Calculating New Q and P
NQ = ((SI+G)-DI)/(PED-PES)
NP = (PED * NQ) + DI

#Printing information
print(" ")
print(f'ORIGINAL QUANTITY = {Q} UNITS')
print(f"ORIGINAL PRICE = £{P}")
print(f"ORIGINAL TOTAL REVENUE FOR FIRM= £{P*Q}")
print(" ")
print(f'NEW QUANTITY = {NQ} UNITS')
print(f"NEW PRICE = £{NP}")
if G > 0:
    print(f"TAX REVENUE FOR GOVERNMENT= £{((NQ * NP)-(NQ*((NP)-(G))))}")#need to fix
    print(f"NEW TOTAL REVENUE FOR FIRM= £{NQ*((NP)-(G))}")#need to fix
else:
    print(f"SUBSIDY SPENDING BY GOVERNMENT= £{((NQ*(NP-G))-(NQ*NP))}")#need to fix
    print(f"NEW TOTAL REVENUE FOR FIRM= £{NP*NQ}")#need to fix

#Idk what these functions do, I copied the internet
fig= plt.figure()
axes= fig.add_axes([0.1,0.1,0.8,0.8])
x= np.arange(0,100)

#Plotting Supply,Demand and Altered Supply
axes.plot(x,((PES * x)+ SI))
axes.plot(x,((PED * x)+ DI))
axes.plot(x,((PES * x)+ SI + G))

#Plotting Price and Quantity
axes.hlines(y=P, xmin=0, xmax=Q, linestyles = '--', colors = 'black')
axes.vlines(x=Q, ymin=0, ymax=P, linestyles = '--', colors = 'black')

#New Price and Quantity
axes.hlines(y=NP, xmin=0, xmax=NQ, linestyles = '--', colors = 'black')
axes.vlines(x=NQ, ymin=0, ymax=NP, linestyles = '--', colors = 'black')

#Plotting Tax/Subsidy Line
axes.hlines(y=NP-G, xmin=0, xmax=NQ, linestyles = '--', colors = 'black')

#Plotting Subsidy Extension
if G < 0:
    axes.vlines(x=NQ, ymin=0, ymax=((PES * NQ)+SI), linestyles = '--', colors = 'black')

#x and y range
axes.set_xlim([0,(-DI/PED)+1])
axes.set_ylim([0,(((PES * NQ)+SI)+1)])

#Showing plot
plt.show()
