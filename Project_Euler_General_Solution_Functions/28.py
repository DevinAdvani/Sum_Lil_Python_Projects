import numpy as np
l = []
for i in range(0,5):
    l.append(0)
matrix = []
for i in range(0,5):
    matrix.append(l)



A = np.matrix(matrix)


print(A[1][2])
