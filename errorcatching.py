"""This is my attempt at creating an errorcatching program"""
#Makes sure the while loop works
#This is so that the try/except thingy repeats so it can try again on an invalid input
true = 1
while true == 1:
    try:
        #Ask for a number
        numba = float(input("Enter a number\n"))
        print(numba, "is a cool number")
        true = 0
    except:
        #This happens if an error occurs at any point within "try:", then loops back to try "try" again.
        print("Not a word or letter.")
