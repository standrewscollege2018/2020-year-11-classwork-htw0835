"""The Tournament, done in class on 27/02/2020"""
#Declare variables and list.
#Glossary: o = opposing
#r = repeat
#u = us/our team
#t = temp variable/not total (confusing i know)
o_team_players = []
o_team_name = "The Placeholders"
r_team_name = True
print("Welcome to the Tournament Calculator.")
while r_team_name == True:
    o_team_name = input("What is the name of the enemy team?\n")
    if o_team_name == "":
        print("Invalid input.")
    else:
        r_team_name = False
r_o_name = True
while r_o_name == True:
    o_name = input("Please enter an enemy team member's name. Enter Admin to end.\n")
    if o_name == "Admin" or o_name == "admin":
        r_o_name = False
    elif o_name == "":
        print("Invalid input.")
    else:
        o_team_players.append(o_name)
print("The enemy team's name is {} and their members are {}".format(o_team_name, o_team_players))
r_games = True
o_points = 0
u_points = 0
t_o_points = 0
t_u_points = 0
while r_games == True:
    try:
        t_o_points = int(input("How many points did the enemy team score this game? Enter -1 to end tournament.\n"))
        if t_o_points != -1:
            t_u_points = int(input("How many points did your team score?\n"))
            if t_o_points > t_u_points:
                o_points += 3
                u_points += 1
                print("The {} won that game.".format(o_team_name))
            elif t_o_points < t_u_points:
                o_points += 1
                u_points += 3
                print("Your team won that team.")
            elif t_o_points == t_u_points:
                o_points += 2
                u_points += 2
                print("It was a draw.")
        else:
            r_games = False
    except:
        print("Invalid input.")
print("End results:\n{} had {} points. You had {} points.".format(o_team_name, o_points, u_points))
if o_points > u_points:
    print("{} won the tournament.".format(o_team_name))
elif o_points < u_points:
    print("You won the tournament.")
elif o_points == u_points:
    print("It was a draw.")