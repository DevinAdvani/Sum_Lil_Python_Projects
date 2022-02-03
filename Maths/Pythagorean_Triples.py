import math

print("7 DIGITS MAXIMUM")

A = int(input("A: "))
B=1

while math.sqrt(A**2 + B**2) != int(math.sqrt(A**2 + B**2)):
    B += 1

C = math.sqrt(A**2 + B**2)

print(f"{A}^2 + {B}^2 = {int(C)}^2")
