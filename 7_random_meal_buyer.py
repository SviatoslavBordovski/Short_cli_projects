# Example input in cli: Mikke, Bobby, Billy, Sam, Peter

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names_list = names_string.split(", ")

#Get the total number of items in list.
num_names = len(names_list)

#Generate random numbers between 0 and the last index. 
random_person = random.randint(0, num_names - 1)

#Pick out random person from list of names using the random number.
bill_payer = names_list[random_person]

print(bill_payer + " is going to buy the meal today!")
