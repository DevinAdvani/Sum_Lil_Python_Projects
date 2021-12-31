import random

#Just a tutorial for the game
rules_check = input("""Do you need an explanation of the rules.
If so type 'yes' in lower case.
If not, type anything else.
INPUT:""")
if rules_check == 'yes':
        print("""
The computer comes up with a code of four numbers ranging from 1 to 4 (by default, one is able to change these variables)
The objective of the game is to guess this code.
You have 10 guesses.
If you run out of these guesses, you lose.
If you guess the correct code before your guesses run out, you win.
After each guess you are given an indication of how many of the numbers are in the right position.
You are also given an indication of how many correct numbers there are, no matter their position.


For example if the code is '1234' and your guess is '1243'.
Every number is correct, however they are in the wrong order.
Therefore correct numbers = 4
However correct number in the correct position is only 2
""")

#Fundamental Replay Loop of Game
Play = True
while Play:

    #Game Settings
    guesses_left = 10
    Highest_Number = 4
    Slots = 4

    #Changing Variables
    change_variables = input("""Would you like to change the settings
If so type 'yes' in lower case.
it not, type anything else.
INPUT:""")
    if change_variables == 'yes':
        guesses_left = int(input("TOTAL GUESSES: "))
        while True:
                Highest_Number = int(input("HIGHEST NUMBER(1-9): "))
                if Highest_Number < 10 and Highest_Number > 0:
                        break
                else:
                        print("INVALID INPUT. NUMBER MUST BE BETWEEN 1 AND 9. TRY AGAIN")
        Slots = int(input("QUANTITY OF NUMBER IN THE CODE: "))

    #Creating the guess list for the while loop to run, creating secret code
    print(f"""CODE IS COMPRISED OF {Slots} NUMBERS, RANGING FROM 0 to {Highest_Number}
THERE ARE {(Highest_Number + 1) ** Slots} DIFFERENT POSSIBLE CODES. GOOD LUCK.""")
    guess = []
    secret_code = []
    for i in range(0,Slots):
            secret_code.append(random.randint(0, Highest_Number))

    #Main Loop
    while guess != secret_code and guesses_left != 0:
        #Just saying how many guesses are left, asking for guess input, turning guess from string to list, and lowering guesses by one each loop
        guess=[]
        print(f"GUESSES LEFT: {guesses_left}")

        #While loop that only breaks when input is appropriate
        while True:
                input0 = input("GUESS:")
                no = "qwertyuiopasdfghjklzxcvbnm!,./;'#[]-=<>?:@~{}_+\|`¬£$%^&*()"
                number_invalid_inputs = []
                for i in range(Highest_Number + 1, 10):
                        number_invalid_inputs.append(i)
                yes = ''.join(str(e) for e in number_invalid_inputs)
                invalid_inputs = yes + no
                if len(input0) == Slots:
                        if not (any(ext in invalid_inputs for ext in input0)):
                                break
                        else:
                                print("INVALID INPUT. TRY AGAIN.")
                else:
                        print("INVALID INPUT. TRY AGAIN.")

        guess = [int(x) for x in str(input0)]
        guesses_left -= 1


        #testing for correct numbers in correct positions


        correct_numbers_in_correct_positions = 0
        for i in range(0,Slots):
            if guess[i] == secret_code[i]:
                correct_numbers_in_correct_positions += 1
        print(f"CORRECT NUMBERS IN CORRECT POSITIONS: {correct_numbers_in_correct_positions}")


        #Testing for correct numbers overall
        correct_numbers_overall = 0
        for i in range (1,Highest_Number+1):
                if guess.count(i) < secret_code.count(i):
                        correct_numbers_overall += guess.count(i)
                else:
                        correct_numbers_overall += secret_code.count(i)

        print(f"CORRECT NUMBERS OVERALL: {correct_numbers_overall}")


    #Congratulate if solved, or reveal correct code if not solved
    if guess == secret_code:
        print(f"Well Done. You solved the code with {guesses_left} guesses left")
    else:
        print(f"Unfortunately you did not solve the code, which was {secret_code}. Better luck next time")

    #Asking Whether they would like to play again
    play_again = input("""To play again, type 'yes' in lower case.
INPUT:""")
    if play_again == "yes":
        Play = True
    else:
        Play = False
