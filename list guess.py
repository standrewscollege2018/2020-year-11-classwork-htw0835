words = ["Cool"]
stop = "N"
while stop != "Y":
    insert = input()
    words.append(insert)
    stop = input("Do you want to stop? Y/N\n")
print(words)