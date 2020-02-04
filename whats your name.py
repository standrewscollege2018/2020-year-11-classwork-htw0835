#Set input to name
name = input("What's your name? >")
#Greet the user along with their name
print("Hello "+name)
#Play da game
print("Let's play the random number game! Guess a number between 1 and 100")
number = random.randint(1,100)
while gnumber != number:
    gnumber = input("What number am I thinking of? >")
    if gnumber < number:
        print("Too low")
    if gnumber > number:
        print("Too high")
    if gnumber == number:
        print("You win!")