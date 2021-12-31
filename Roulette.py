from random import randrange

round0 = 1
money = 10
bet = 0


print(f"""WELCOME TO ROULETTE WITH AN EXACTLY 50/50 CHANCE.
YOU START THE GAME WITH £10.
MAKE A BET.
YOU KEEP ON GOING UNTIL YOU RUN OUT OF MONEY
""")

while money > 0:
    money = round(money,4)
    print(f"""ROUND {round0}
MONEY: £{money}""")
    while True:
        bet = float(input("MONEY BET: £"))
        if(float(bet) > 0 and float(bet) < (float(money)+0.01)):
            money -= bet
            break
    if(randrange(2)) == 0:
        bet *= 2
        money += bet
        round0 += 1
        print(f"YOU WON £{bet}")
    else:
        bet = 0
        round0 += 1
        print("YOU LOST")
