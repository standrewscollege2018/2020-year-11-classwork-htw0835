#Fake inputs
what_buying = input("What are you looking to buy? >")
itemprice = float(input("How much does it cost? >"))
GST = 0.15
#Print out insult
print("You want to buy a " + what_buying +"? What a loser. Only morons would buy something like that. Honestly, I'm surprised that your brain functions enough to even use the keyboard to run this program.")
answer = input("Are you sorry? Tell me, worm. >")
print("I don't care if you said ", answer + ", because only a brainless whelp would respond to me with something like that. Also, your total is", itemprice * (1 + GST))
print()