"""This program takes the user's input of an integer and multiplies it by 1024 multiple times to get an amount of bytes"""
#User input
giga = int(input("Enter a whole number of gigabytes >"))
#Print the amount
print("Gigabytes = {}\nMegabytes = {}\nKilobytes = {}\nBytes = {}".format(giga, giga * 1024, giga * 1024 * 1024, giga * 1024 * 1024 * 1024))