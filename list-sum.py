"""This is the list-sum exercise."""
#declare variables and list
int_input = 0
int_list = []
#intro message
print("While prompted to input, enter -1 to end program and print results.")
#begin while loop
while int_input != -1:
    #recieve input
    int_input = int(input("Enter a number.\n"))
    #if the input is not -1 (if it was -1, it would subtract 1 from the final print() without this if statement)
    if int_input != -1:
        #add input to list
        int_list.append(int_input)
#repeat this once for each item in list
for i in range(0,len(int_list)):
    #print the current number where i = place in list
    print(int_list[i])
#print the sum of list
print(sum(int_list))