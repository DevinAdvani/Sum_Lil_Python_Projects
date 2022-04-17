#composite is a number that can be written as the product of two smaller positive integers 8 = 2 * 4
composite = []
for i in range(3,100,2):
    for j in range(3,100,2):
        composite.append(i*j)
print(sorted(list(set(composite))))

def Gb(x):
    #prime plus a square
