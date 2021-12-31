from random import randrange

#Need to clean up inputs, like no negative bets and shit like that. but main body is here to automate.

#Giving a card to the dealer
def card_to_dealer():
    r = randrange(len(cards))
    dealer.append(cards[r])
    cards.remove(cards[r])

#Giving a card to your hand
def card_to_hand():
    r = randrange(len(cards))
    hand.append(cards[r])
    cards.remove(cards[r])

#Giving a score to your hand - need to prevent it permanently turning J into 10
def Score(d):
    n = d
    for i in range(0, len(n)):
        if n[i] == 'A' or n[i] == 'K' or n[i] == 'Q' or n[i] == 'J':
            n[i] = 10
    return sum(n)



#Settings
decks = 1
cards= []
used = []
dealer = []
hand = []
hand_score = 0
dealer_score = 0
bet = 0
money = 10

#Creating a deck
for d in range (0,decks):
    for s in range (0,4):
        for n in range(2,11):
            cards.append(n)
        cards.append('J')
        cards.append('Q')
        cards.append('K')
        cards.append('A')

while money > 0:
    #Dealing Cards
    card_to_dealer()
    card_to_dealer()
    card_to_hand()
    card_to_hand()

    #Bet
    bet = input(f"YOU HAVE £{money}. BET: ")
    money -= float(bet)

    #Score calculation
    hand_score = Score(hand)
    dealer_score = Score(dealer)


    #Information
    print(f"""YOUR HAND: {hand}
    DEALER HAND: [{dealer[0]}, UNKNOWN]""")

    #Setting Loss to False
    Player_Loss = False
    Dealer_Loss = False

    #Hitting
    hit_count = 0
    while hit_count < 3:
        hit = input("""Type in 'h' in lower case if you would like to hit.
    If not, type anything else.
    INPUT: """)
        if hit == 'h':
            card_to_hand()
            print(f"YOUR HAND: {hand}")
            hit_count += 1
        else:
            break
        if Score(hand) > 21:
            Player_Loss = True
            print("YOU LOSE")
            bet = 0
            break
            
    #Dealer Playing
    hit_count = 0
    print(f"DEALER HAND: {dealer}")
    while hit_count < 3 and dealer_score < 16 and Player_Loss == False:
        card_to_dealer()
        dealer_score = Score(dealer)
        print(f"DEALER HAND: {dealer}")
        hit_count += 1
        if Score(dealer) > 21:
            Dealer_Loss = True
            print("YOU WIN")
            money += (2 * float(bet))
            bet = 0
            break

    #Comparing Player and Dealer
    if Player_Loss == False and Dealer_Loss == False:
        if Score(dealer) == Score(hand):
            print("DRAW")
            money += float(bet)
            bet = 0
        if Score(dealer) > Score(hand):
            print("YOU LOSE")
            bet = 0
        if Score(dealer) < Score(hand):
            print("YOU WIN")
            money += (2 * float(bet))

    #Moving cards to discard pile
    used.extend(hand)
    used.extend(dealer)
    hand=[]
    dealer=[]


    #Reshuffle
    if len(used) > len(cards):
        print("RESHUFFLE")
        used = []
        cards = []
        for d in range (0,decks):
            for s in range (0,4):
                for n in range(2,11):
                    cards.append(n)
                cards.append('J')
                cards.append('Q')
                cards.append('K')
                cards.append('A')





