primes = [2,3,5,7,11,13,17]
list= []

for i in range(100,1000):
    if i % 2 == 0 and str(i)[0] != str(i)[1] and str(i)[1] != str(i)[2] and str(i)[0] != str(i)[2]:
        list.append(i)

print(list)
