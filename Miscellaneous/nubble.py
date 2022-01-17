#Credit for idea goes to me
#Credit for actually building goes to Ryan

# Imporing the functions permutations and combinations

from itertools import permutations, combinations



# Creating a list that contains all the permutations of "abcd"

perms = [''.join(p) for p in permutations("abcd")]



# Creating a list, dotperms, which adds the symbols ".", ",", "?" in between each of the letters to be replaced by an operation later on

dotperms = []

for i in range(len(perms)):

    dotperms.append(f"{perms[i][0]}.{perms[i][1]},{perms[i][2]}?{perms[i][3]}")



# Creating a list, perm_operations, that contains all the permutations of any order of operations

operations = list(set(list(combinations(["+", "+", "+", "-", "-", "-", "*", "*", "*", "/", "/", "/"], 3))))

perm_operations = []

for i in range(len(operations)):

    perm_operations.append(set([''.join(p) for p in permutations(f"{operations[i][0]}{operations[i][1]}{operations[i][2]}")]))



# Creating a new list, equation, that has every possible equation without brackets

equation = []

for i in dotperms:

    for j in perm_operations:

        for k in j:

            equation.append(i.replace(".", k[0]).replace(",", k[1]).replace("?", k[2]))



# Now creating a new list, equation_brackets, that contains every possible equation with brackets

equation = set(equation)

equation_brackets = []

for i in equation:

    equation_brackets.append(i)                                 #a.d.c.d

    equation_brackets.append(f"({i[0:3]}){i[3:]}")              #(a.d).c.d

    equation_brackets.append(f"{i[0:2]}({i[2:5]}){i[5:]}")      #a.(d.c).d

    equation_brackets.append(f"{i[0:4]}({i[4:]})")              #a.d.(c.d)

    equation_brackets.append(f"(({i[0:3]}){i[3:5]}){i[5:]}")    #((a.d).c).d

    equation_brackets.append(f"({i[0:2]}({i[2:5]})){i[5:]}")    #(a.(d.c)).d

    equation_brackets.append(f"{i[0:2]}(({i[2:5]}){i[5:]})")    #a.((d.c).d)

    equation_brackets.append(f"{i[0:2]}({i[2:4]}({i[4:]}))")    #a.(d.(c.d))

    equation_brackets.append(f"({i[0:3]}){i[3:4]}({i[4:]})")    #(a.d).(c.d)

    equation_brackets.append(f"({i[0:5]}){i[5:]}")              #(a.d.c).d

    equation_brackets.append(f"{i[0:2]}({i[2:]})")              #a.(d.c.d)



# The 4 inputs

a, b, c, d = int(input("First number: ")), int(input("Second number: ")), int(input("Third number: ")), int(input("Fourth number: "))



# Converting the strings of every equation into executable code using eval() whilst checking for division by zero

nubble_numbers = []

for i in equation_brackets:

    try:

        num = eval(i)

    except ZeroDivisionError:

        continue

    if 100 >= num and num > 0 and num == int(num):

        nubble_numbers.append(int(num))



# Prints all nubble numbers :D

for i in sorted(set(nubble_numbers)):

    print(i)

while True:
    Var = 1
