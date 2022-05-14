primes = [2,3,5,7,11,13,17]
primelist = []
for j in primes:
    list = []
    for i in range(100,1000):
        if i % j == 0 and str(i)[0] != str(i)[1] and str(i)[1] != str(i)[2] and str(i)[0] != str(i)[2]:
            list.append(i)
    primelist.append(list)


for a in range(0,6):
    for i in primelist[a]:
        for j in primelist[a+1]:
            if str(i)[1:3] == str(j)[0:2]:
                print(a,a+1,i,j)
