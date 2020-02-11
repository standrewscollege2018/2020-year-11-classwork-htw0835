#I copied this code from onenote
keepasking = True
while keepasking == True:
    name = input("Enter name:\n")
    if name == "stop":
        keepasking = False
    else:
        print("Hello", name)
