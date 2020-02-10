"""Blood donor made in class on 10/2/2020"""

#setting global variable
MINIMUM_AGE = 16
MIN_BODY_WEIGHT = 50

#Get input
age = int(input("How old are you?\n"))
weight = int(input("How much do you weigh, in KGs?\n"))

#The statement itself
if age >= MINIMUM_AGE and weight >= MIN_BODY_WEIGHT:
    print("You can donate blood")
else:
    print("You cannot donate blood")

