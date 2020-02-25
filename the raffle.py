#Import random package
import random
#Declare list & variables
participants = []
keepasking = True
random_particip = 0
#Intro output
print("Enter 'Admin' to draw from the names")
#begin loop until "Admin" is entered. This loop never ends

while keepasking == True:
        #Ask user for input
        new_particip = input("What is your name?\n")
        #If user inputs "Admin" or "admin"
        if new_particip == "Admin" or new_particip == "admin":
                #Ends loop
                keepasking = False
        else:
                #Append user input to list
                participants.append(new_particip)
rand_particip = random.randint(0,len(participants))
print(participants[rand_particip], "wins the raffle!")