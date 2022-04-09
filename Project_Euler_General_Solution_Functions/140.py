def G(k):#Basically just the nth fibonacci number with the first numbers being one and four
    ks = [1,4]
    if k == 1:
        return 1
    if k == 2:
        return 4
    while len(ks) != k:
        ks.append(ks[-1]+ks[-2])
    return ks[-1]

def AG(x):#input x into the function with o being the order, i.e. the final power
    sum = 0
    for n in range(1,101):
        sum += (x**n)*(G(n))
    return round(sum)

def C(n):# the calibration
    x = 1000000000
    inputs = []
    outputs = []
    inputs.append(0)
    outputs.append(AG(0))
    while n != AG(x):
        inputs.append(x)
        outputs.append(AG(x))
        x =
    return x
