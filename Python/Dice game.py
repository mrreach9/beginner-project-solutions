
import random
while True:
    sides = input("How many sides would you like your die to have?  ")
    times = input("How many times should I roll it for you?  ")
    try:
        sides = int(sides)
        times = int(times)
        roll = 0
        rolls = 0
        while rolls < times:
            number = random.randint(1, sides)
            roll += number
            rolls += 1
            print ("Roll {rolls}: {number}".format(rolls=rolls, number=number))
        print ("Total = {roll}".format(roll=roll))
    except:
            print("Please enter valid numbers next time.")
    again = input("Would you like to roll again? Y/N: ")
    if again.upper() == 'Y':
        continue
    elif again.upper() == 'N':
        quit()
