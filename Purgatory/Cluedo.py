#Creating initial deck of cards
persons = ['mustard','plum','green','peacock','scarlett','white']
weapons = ['dagger','candlestick','revolver','rope','leadpipe','spanner']
rooms = ['hall','lounge','dining','kitchen','ballroom','conservatory','billiard','library','study']

#Creating lists of everyones possible cards
cards0 = []
secret = persons + weapons + rooms
idk = secret

#Input your own cards
input0 = ''
print(f"""INPUT YOUR HAND IN LOWER CASE AND ONE WORD.
EXAMPLES: {persons},{weapons},{rooms}
ONCE FINISHED, TYPE IN 'done'.""")
while input0 != 'done':
    input0 = input('INPUT: ')
    cards0.append(input0)
cards0.remove('done')


#What is each players name
P1 = input("What is player 1's name: ")
P2 = input("What is player 2's name: ")
P3 = input("What is player 3's name: ")

#creating possible cards of everyone else
cards1 = persons + weapons + rooms
cards2 = persons + weapons + rooms
cards3 = persons + weapons + rooms

#Removing your cards from everyone elses
cards1 = set(cards1) - set(cards0)
cards2 = set(cards2) - set(cards0)
cards2 = set(cards2) - set(cards0)

#Certain cards that people have
ccards1 = []
ccards2 = []
ccards3 = []

#Creating dictionnary for recording peoples answers to inquiries
inquiries = {}
i = 0

#Central Program
while True:
    choice = input("""
type 'a' if you were shown a card by someone
type 'b' if someone did not have some cards
type 'c' if someone did show some cards to someone else
INPUT: """)
    #Shown cards
    if choice == 'a':
        card_shown = input("card shown: ")
        player = input("name of player who showed: ")
        if player == P1:
            ccards1.append(card_shown)
        if player == P2:
            ccards2.append(card_shown)
        if player == P3:
            ccards3.append(card_shown)
    #Not shown cards
    if choice == 'b':
        person = ''
        person = input("who: ")
        if person == P1:
            remove =[]
            input1 = ''
            print(f"same rules as start. {persons},{weapons},{rooms}")
            while input1 != 'done':
                input1 = input('INPUT: ')
                remove.append(input1)
            remove.remove('done')
            cards1 = set(cards1) - set(remove)
        if person == P2:
            remove =[]
            input2 = ''
            print(f"same rules as start. {persons},{weapons},{rooms}")
            while input2 != 'done':
                input2 = input('INPUT: ')
                remove.append(input2)
            remove.remove('done')
            cards2 = set(cards2) - set(remove)
        if person == P3:
            remove =[]
            input3 = ''
            print(f"same rules as start. {persons},{weapons},{rooms}")
            while input3 != 'done':
                input3 = input('INPUT: ')
                remove.append(input3)
            remove.remove('done')
            cards3 = set(cards3) - set(remove)
    if choice == 'c':
        i += 1
        files = []
        input4 = ''
        print(f"same rules as start. {persons},{weapons},{rooms}")
        while input4 != 'done':
            input4 = input('INPUT: ')
            files.append(input4)
        files.remove('done')
        person = ''
        person = input("who: ")
        if person == P1:
            inquiries[i] = [P1, files]
        if person == P2:
            inquiries[i] = [P2, files]
        if person == P3:
            inquiries[i] = [P3, files]


    #Need to add if card was shown directly and if it was shown to someone else

    #Removing shown cards from everyone's cards
    cards1 = set(cards1) - set(ccards2)
    cards1 = set(cards1) - set(ccards3)
    cards2 = set(cards2) - set(ccards1)
    cards2 = set(cards2) - set(ccards3)
    cards3 = set(cards3) - set(ccards1)
    cards3 = set(cards3) - set(ccards2)

    #Deriving possible secret cards
    secret = set(secret) - set(cards0) - set(ccards1) - set(ccards2) - set(ccards3)

    #Showing impossible cards
    icards1 = set(idk) - set(cards1)
    icards2 = set(idk) - set(cards2)
    icards3 = set(idk) - set(cards3)

    #If two cards are impossible, then the only possible card is inferred


    #state if card is solved

    #Display
    print(f"""
YOUR CARDS: {cards0}
{P1} CARDS: {ccards1}
{P2} CARDS: {ccards2}
{P3} CARDS: {ccards3}
{P1} POSSIBLE CARDS: {cards1}
{P2} POSSIBLE CARDS: {cards2}
{P3} POSSIBLE CARDS: {cards3}
{P1} IMPOSSIBLE CARDS: {icards1}
{P2} IMPOSSIBLE CARDS: {icards2}
{P3} IMPOSSIBLE CARDS: {icards3}
POSSIBLE SECRET CARDS: {secret}
INQUIRIES: {inquiries}
""")
