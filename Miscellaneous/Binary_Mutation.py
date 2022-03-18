import math

#copied function that basically turns a character into binary
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m


code = input("ENTER A STRING: ")

print(Binary(code))
