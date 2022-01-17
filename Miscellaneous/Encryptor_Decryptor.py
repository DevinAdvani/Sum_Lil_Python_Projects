import string
alphabet_string = string.ascii_lowercase #Create a string of all lowercase letters
alphabet_list = list(alphabet_string) #Create a list of all lowercase letters

#creating a list of every possible input and output
inputs = alphabet_list
outputs = []

#Creating code key
for i in range(0,26):
    display = inputs[i]
    input0 = 0
    while True:
        input0 = input(f"TURN {display} TO:  ")#add remaining keys
        if not input0 in outputs and input0 in inputs:
            break
    outputs.append(input0)

#Adding Spaces
inputs.append(' ')
outputs.append(' ')

#code input
code = input("ENTER CODE ALL IN LOWER CASE TO ENCRYPT: ")

#encryption
encrypted = ''
for i in range(0,len(code)):
    E = outputs[inputs.index(code[i])]
    encrypted += (E)
print(encrypted)

#code input
code = input("ENTER CODE ALL IN LOWER CASE TO DECRYPT: ")

#decryption
decrypted = ''
for i in range(0,len(code)):
    D = inputs[outputs.index(code[i])]
    decrypted += (D)
print(decrypted)

#Kepp on running
while True:
    var = 100
