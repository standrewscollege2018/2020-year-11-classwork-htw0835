"""Silent auction."""
loop = 0
#Ask for inputs at the start
while loop == 0:
        try:
                item = input("What are you bidding for?\n")
                reserve_price = float(input("What is the reserve price?\n"))
                loop = 1
        except:
                print("That is invalid. Try again.")
#I'm setting the variables here for some reason
highest_name = "God"
highest_price = int(0.00)
recursive = 0
LOOPTHISFOREVER = 0
#AUCTION START
print("The auction has started! Enter -1 when asked for price to end auction.\n \n Highest bid so far is", highest_price)
#Loop that allows the program to continue even after an error
while recursive == 0:
        #Try and except...
        try:
                #Ask user's name and price
                repeatnaming = 0
                while repeatnaming == 0:
                        name = input("What's your name?\n")
                        if name == "":
                                print("Please try again with a valid input.")
                        else:
                                repeatnaming = 1
                price = float(input("How much are you bidding?\n"))
                if price == -1:
                        recursive = 1
                        print("End of auction. {} wins.".format(highest_name))
                        repeatnaming = 0
                elif price == 69:
                        while LOOPTHISFOREVER == 0:
                                print("BananaBread")                
                #If your price is higher than both the reserve AND the highest price...
                elif price > highest_price and price > reserve_price:
                        highest_price = price
                        highest_name = name
                        print("Highest bid so far is {} at {}".format(highest_name, highest_price))
                        price = 0
                        name = 0
                        repeatnaming = 0
                #If it doesn't...
                else:
                        print("That bid is too low.\nHighest bid so far is {} at {}".format(highest_name, highest_price))
                        repeatnaming = 0
                #This happens when the user wants to exit.
        except:
                #Error message
                print("You have entered something invalid. Please try again.")
                repeatnaming = 0