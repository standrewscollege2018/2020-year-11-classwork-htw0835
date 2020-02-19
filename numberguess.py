"""Please never use this program. This program hates you and you will never be able to reach the end of it."""
#import random
import random
#Set variables
loopgram = 0
while loopgram == 0:
    try:
        number = random.randint(1,100000000)
        #MAKE NEXT LINE A COMMENT WHEN NOT DEBUGGING
        #print(number)
        solved = 0
        guessed = 0
        #Ask for initial input
        guess_number = int(input("Let's play a game, whelp. I'm thinking of a number between 1 and 100,000,000.\n"))
        #Start the loop
        while solved == 0:
            if guess_number > number:
                #If too high...
                print("That is too high, and your family doesn't love you.")
                guessed += 1
            elif guess_number == number:
                #Win!
                print("Good job.")
                solved = 1
            else:
                #If too low...
                print("That is too low, and your pets are going to die before you do.")
                guessed += 1
            if solved == 0:
                #Ask again if not solved
                guess_number = int(input("Try again, idiot moron.\n"))
        #You aren't done yet
        solved = 0
        #This is gonna suck for you
        #MAKE NEXT LINE A COMMENT WHEN NOT DEBUGGING
        #print(number/guessed)
        guess_number = float(input("Now try this game: the new number you have to guess is my original number divided by the amount of guesses you had.\nAnd no counting them!\nAlso, the guesses you make during this game count too.\n"))
        #Start the second game
        while solved == 0:
            if guess_number > (number/guessed):
                #If too high...
                print("Wrong. You're a failure to your ancestors.")
                guessed += 1
            elif guess_number == (number/guessed):
                #Wow!
                print("You did it. I'm surprised.")
                loopgram = 1
                solved = 1
            else:
                #If too low...
                print("Nuh-uh. Your parents wished they homeschooled you.")
                guessed += 1
            if solved == 0:
                #Ask again if not solved
                guess_number = int(input("Give it another shot, you're amusing me.\n"))
    except:
        #Sends naughty boys back
        print("You're trying to break my code, are you? Shame. Go back to the start.")