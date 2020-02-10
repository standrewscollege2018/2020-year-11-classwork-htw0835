"""This is a test to see what happens if i make a neverending for loop"""
#Setting variables
variable = 1
upordown = 1

#Defining upordown
#I do this so that I can make variable go up or down depending on how large it is
if variable > 5:
    upordown = -1
else:
    upordown = 1
    
#Run
for variable in range(0, 10, upordown):
    print(variable)