import math

theta = 2.956938891377988

b = [theta]

for i in range(0,24):
    b.append(math.floor(b[-1])*(b[-1]-math.floor(b[-1])+1))

a = []

for x in b:
    a.append(str(math.floor(x)))

print(''.join(a))

#make a function that returns the original theta minus the concenated string
#then binary search tree that
