import random

computer_tries = 0
player_number = None
computer_guess = random.randint(1, 100)

print(
    """
    Welcome Player to the fabulous number guessing game.
    Please allow me to show you my incredible deduction skills
    """)

question = None
while question != ("yes"):
    question = input("Has the player picked a number? ")
    question = question.lower()
    if question == "yes":
        print("\nI will now guess your number!!!\n")
        while player_number == None:
            computer_tries += 1
            print(computer_guess, "\n")
            confirmation = input("Is this the correct number? ")
            confirmation = confirmation.lower()
            if confirmation == "yes":
                player_number = computer_guess
                if computer_tries < 2:
                    print("I did it! I guessed your number was", computer_guess,
                           "and it only \ntook me", computer_tries,
                           "try to get it right!")
                else:
                    print("I did it! I guessed your number was", computer_guess,
                           "and it only \ntook me", computer_tries,
                           "tries to get it right!")
            else:
                higher_lower = None
                while higher_lower not in ("higher", "lower"):
                    higher_lower = input("Is my guess higher or lower"
                                + " than your number? ")
                    higher_lower = higher_lower.lower()
                    if higher_lower == "higher":
                        higher = computer_guess
                        computer_guess = random.randint(higher, 101)
                    elif higher_lower == "lower":
                        lower = computer_guess
                        computer_guess = random.randint(0, lower)
                    else:
                        print("Please choose either higher or lower.")



input("\n\nPress the enter key to exit")
