def PC(a):
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

#assemble all the different permutations of numbers for different digit lengths
#then do a prime checker
digits = [1,2,3,4,5,6,7,8,9]
