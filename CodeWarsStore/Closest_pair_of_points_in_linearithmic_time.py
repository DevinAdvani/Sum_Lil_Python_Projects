import math
import random

def close(x1,y1,x2,y2,distance):
    if x1-distance < x2 < x1+distance:
        if y1-distance < y2 < y1+distance:
            return True
        else:
            return False
    else:
        return False

def closest_pair(points):
    for i in range(0,len(points)):
        for j in range(0,len(points)):
            if i != j:
                if points[i] == points[j]:
                    return [points[i],points[j]]
    points = list(points)
    while len(points) > 2:
        n = random.randrange(len(points))
        D = 10000000
        for i in range(0,len(points)):
            d = math.hypot(points[n][0]-points[i][0],points[n][1]-points[i][1])
            if d < D and d != 0:
                D = d
        dist =  3/2 * d/(2 * (2 ** 0.5))
        store = []
        while len(store) < 1:
            for i in range(0,len(points)):
                count = 0
                for j in range(0,len(points)):
                    if i != j:
                        if close(points[i][0],points[i][1],points[j][0],points[j][1],dist):
                            count += 1
                if count == 0:
                    store.append(points[i])
            points = list(set(points)- set(store))

    return points
