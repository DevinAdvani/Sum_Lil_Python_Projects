from random import randrange

round0 = 1
money = 10
bet = 0
con_loss = 0


print(f"""THIS IS A ROULETTE SIMULATION.
THERE IS A ROULETTE GAME, HOWEVER THE COMPUTER AUTOMATICALLY GAMBLES £0.01.
HOWEVER FOR EACH TIME THEY LOSE, THEIR GAMBLE DOUBLES.
IF THEY WIN, IT GOES BACK TO ZERO.
I JUST WANT TO SEE HOW MUCH MONEY THEY CAN MAKE BEFORE GOING BANKRUPT.
""")

while money > 0:
    money = round(money,4)
    print(f"""ROUND {round0}
MONEY: £{money}""")
    while True:
        bet = (0.01 * (2 ** con_loss))
        if(float(bet) > 0 and float(bet) < (float(money)+0.01)):
            print(f"BET = {bet}")
            money -= bet
            break
    if(randrange(2)) == 0:
        bet *= 2
        money += bet
        round0 += 1
        con_loss = 0
        print(f"YOU WON £{bet}")
    else:
        bet = 0
        round0 += 1
        print("YOU LOST")
        con_loss += 1
        
