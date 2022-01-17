import random
#A simulation of how a population would survive under evolutionary change
#i.e. Elephants with tusks getting hunted
Tusks = int(input("NUMBER OF TUSKS: "))
Non_Tusks = 0
Pop_Growth = float(input("POPULATION GROWTH RATE: "))
Mut_Chance = float(input("MUTATION CHANCE: "))
Tusks_Hunted = int(input("TUSKS HUNTED EACH GENERATION: "))
Pop_Lim = int(input("POPULATION LIMIT: "))
Mutants = 0
Gen = 0
Gen_Limit = int(input("GENERATION LIMIT: "))

#Simulation
while Tusks > 0 and Gen < Gen_Limit:
    print(f"""GENERATION {Gen}
{Tusks} Tusked Elephants
{Non_Tusks} Non-Tusked Elephants
""")
    Tusks *= Pop_Growth
    Non_Tusks *= Pop_Growth
    Tusks = int(Tusks)
    Non_Tusks = int(Non_Tusks)
    Gen += 1
    Tusks -= Tusks_Hunted
    for i in range(0, int(Tusks * (Pop_Growth -1))):
        if random.random() < Mut_Chance:
            Non_Tusks +=1
    while Tusks+Non_Tusks > Pop_Lim:
        if random.random() < (Tusks/(Non_Tusks+Tusks)):
            Tusks -= 1
        else:
            Non_Tusks -= 1


input("")
