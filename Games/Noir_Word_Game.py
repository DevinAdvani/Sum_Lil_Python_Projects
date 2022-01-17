#Statement 1 / Intro
print("For choice decisions, type in the corresponding number")

#Basic Loop 1
choice = 0
while True:
    choice = input("""Do you understand?
[1] - yes
[2] - no
""")
    if choice == '1':
        print("Correct answer. Good luck on your story")
        break
    elif choice == '2':
        print("Lying can take you far, but it can also be the death of you. Be careful on your story.")
    else:
        print(f"Try again you dweeb")

#Registering name
name = input("What's your name: ")
print(f"Hello traveller {name}")

#Basic Loop 2
choice = 0
while True:
    choice = input("""Are you ready to go on an adventure?
[1] - yes
[2] - no
""")
    if choice == '1':
        print("Have fun, but be careful")
        break
    elif choice == '2':
        print(f"Stop being a bitch, {name}")
    else:
        print(f"Try again {name}, you dweeb")

#Statement 2 / Location description
print("""DATE:       15 JANUARY 1965
LOCATION:   THE DREW CLUB, NEW YORK
You sit in a dusty club tasting cigarette smoke.
And then she walked in.""")

#Basic Loop 3
choice = 0
while True:
    choice = input("""[1] - You go up to her and ask her name
[2] - You stay at your table sipping whisky
""")
    if choice == '1':
        print(f"""You introduce yourself as Young {name}.
She laughs and introduces herself as Sophia.
You buy her a drink.
Vodka on ice.""")
        break
    elif choice == '2':
        print(f"""Eventually the girl leaves.
Soon you realise you'll never be able to forget those delicious curvaceous thighs.
So you leave the club and try to find her for a full month.
From time to time you think you see her. But it's never her.
Eventually on a dark night a bottle of whisky and some rope get the better of you.
GAME OVER



Try again:""")

    else:
        print(f"Try again {name}, you dweeb")

#Statement 3 / A situation
print("While you talk to her and while she laughs at your jokes you sense someone standing behind you.")

#Basic Loop 4
choice = 0
while True:
    choice = input("""[1] - You ignore the person and keep on talking to your future wife
[2] - You turn around to glance at this madman
""")
    if choice == '1':
        print(f"""As you continue to talk to her you feel something cold and sharp enter your back.
Your eyes go wide. You look behind at the person, but there's no one there.
You look at her blue eyes and smile for the last time. You die with a boner and a beautiful woman next to you.
Not bad, but
GAME OVER



Try again:""")
    elif choice == '2':
        print(f"""You turn around, but the shadowy person behind growls. "Hold it bub, What do you think you're doing talking to my top bitch."
You look at Sophia, but she doesn't hold eye contact. Jesus you think to yourself.""")
        break
    else:
        print(f"Try again {name}, you dweeb")

#Statement 4 / A situation
print("""The man drags her off of her seat. You wait a minute and then follow them to a dusty flat.
You stand looking at the flat on the opposite street. It's on the ground floor.
You hear screaming from inside the flat.""")

#Basic Loop 5
choice = 0
while True:
    choice = input("""[1] - You try and enter the flat through the main entrance
[2] - You try and enter the flat through the window
""")
    if choice == '1':
        print(f"""You manage to enter into the flat's public area by sneaking in after someone who just entered.
You keep moving until you find the flat where the screaming is occuring. You kick down the door and enter the room and look towards the screaming.
The man stands over the woman with a knife. His eyes glinting darkly. Cigarette in mouth.
According to the newspaper reports a few days later about the incident, the pimp was an artist. He emulated Jackson Pollocks.
His knife was a paintbrush. The woman his canvas. Her blood the paint.""")
        break
    elif choice == '2':
        print(f"""You take your jacket off and wrap it around your hand. You manage to break a window. But when pulling you arm out, you cut your wrist.
Badly. Very Badly. Extremely fucking badly. Jesus, you cut a major artery. Blood sprays everywhere. You faint and pass onto the next life.
The loss of blood does manage to get rid of your boner though.
GAME OVER



Try again:""")
    else:
        print(f"Try again {name}, you dweeb")

#Statement 5 / Another situation
print("""He tosses her limp body to the floor and charges towards you. You shake yourself out of disbelief and look around the room for weapons.""")

#Basic Loop 6
choice = 0
while True:
    choice = input("""[1] - A chair
[2] - Fuck him, you're gonna kill him just with your bare hands
""")
    if choice == '1':
        print(f"""He attempts to stab you, but you block him with chair. He tries to pull the knife out, but he's not strong enough.
You kick him and he falls to the floor. You raise the chair and bring it down upon him. He tries to stand up, but you keep beating it down upon him.
Until he can no longer struggle. Once that is done, you walk to Sophia, or some vague resemblance of her that doesn't breathe anymore.
You clutch her in your arms, but you hear police sirens. You exit out of the flat and walk away. Where?""")
        break
    elif choice == '2':
        print(f"""You enter a fighting stance and wait for him to come closer. He charges closer and closer. A wild smile on his face.
He jumps towards you, knife in hand. You attempt to catch his arm, but you misjudge and the knife goes through your right hand and pins you to the wall behind you.
You attempt to pull the knife out, but you're not strong enough. He steps away finds a gun in his drawer and points it towards you.
In your moments before the complete and utter darkness of death, you don't feel fear, but  merely sadness for what could have been.
GAME OVER



Try again:""")
    else:
        print(f"Try again {name}, you dweeb")

#Statement 6 / La fin
print("""God knows.


La Fin""")

while True:
    var = 1
