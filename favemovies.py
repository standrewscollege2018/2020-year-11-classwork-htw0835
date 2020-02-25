"""This is the favorite movies exercise using lists."""
#Intro line
print("Enter your 3 favorites movies, from favorite to least favorite.")
#Sorting out that the variable movie_list is a list
#This is so that movie_list.append will word expectedly
movie_list = []
#Repeat three times
for i in range(0,3):
    append_to_list = input("Enter a movie\n")
    movie_list.append(append_to_list)
#Prints raw list
print(movie_list)
#Makes the list all purty
print("\nFavorite movie one:", movie_list[0], "\nFavorite movie two:", movie_list[1], "\nFavorite movie three:", movie_list[2])
#Second part
second_thoughts = input("Are you having second thoughts about your list? Y/N \n")
if second_thoughts == "Y" or "y":
    replace = int(input("Which item on the list do you want to replace? \n"))
    if -1 < replace <= 3:
        replace_with = input("What are you replacing it with? \n")
        movie_list.insert(replace-1,replace_with)
        movie_list.pop(replace)
    else:
        print("You have entered something out of range. You cannot replace anything anymore.")
    #Prints raw list
    print(movie_list)
    #Makes the list all purty
    print("\nFavorite movie one:", movie_list[0], "\nFavorite movie two:", movie_list[1], "\nFavorite movie three:", movie_list[2])