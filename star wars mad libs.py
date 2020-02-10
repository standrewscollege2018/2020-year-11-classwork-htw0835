"""This is my attempt at doing Mad Libs for class."""

#Opening line
print("Starwars Mad Libs by someone who never watched Star Wars \n")
#Take player's input to make variables
name1 = input("Enter a cool name\n")
name2 = input("Enter a lame name\n")
adjective1 = input("Enter a 'good' adjective\n")
adjective2 = input("Enter a 'bad' adjective\n")
color1 = input("Enter a color\n")
color2 = input("Enter a color\n")
noun1 = input("Enter a noun\n")
noun2 = input("Enter another noun\n")
verb1 = input("Enter a verb ending in -ed\n")
verb2 = input("Enter another verb ending in -ed\n")
name3 = input("Enter a female name\n")
verb3 = input("Enter another verb\n")
galaxy = input("Enter a weird name\n")
#Makes the story
print("Your story: \n \n {} and {} were having a battle on the big ship. {} was an agent of the sith, the {} side. But {} was from their sworn enemies, the jedi, the {} side. They had their light sabers. {}'s was {} and {}'s was {}. Suddenly {} pulled out his secret weapon, his {} and {} before using it on {}. {} was on the brink of defeat before he pulled out his very own {} and {} {} and made sure he never was {} again, because that is how the sith are {} and that is bad. But he was {} and that is a good thing because the jedi are good. That is how star wars works. He went to the big prison place on the ship and found {} in her cell, {}. He opened the cell and she went ''Yay! You saved the {} galaxy, {}!'' and then they hugged and went away and didn't do anything else because they were siblings. But {} was still alive when they passed him by and he said ''{} {}... I am you daddy'' but neither of them cared that much. They got an award for saving the {} galaxy. The end!!!".format(name1, name2, name1, adjective2, name2, adjective1, name1, color1, name2, color2, name1, noun1, verb1, name2, name2, noun2, verb2, name1, adjective2, adjective2, adjective1, name3, verb3, galaxy, name2, name1, name2, name3, galaxy))