import itertools

def f(x):#where x is x by x grid
    single = []
    for i in range(0,x):
        single.append("R")
        single.append("D")
    return len(set(list(itertools.permutations(single))))




#multiple of two as paths are reflections
print(f(6))
