# ask the users to enter the type of things they want to bring to a party

# create a list to store the choices
choices = []
while True:
    choice = input("Enter something you want to bring to the party: ")
    choices.append(choice)
    # ask the user if they want to add more items
    more = input("Do you want to add more? (y/n): ")
    if more.lower() != "y":
        break

print("You want to bring some of these", len(choices), "things to the party.")
print(choices)


# ask user how many total items they want to bring
total_number_of_items = int(input("How many things do you want to bring to the party in total? "))  

# calculate how many different ways there would be to fill the slots
number_of_permutations = len(choices) ** total_number_of_items

print("There are", number_of_permutations, "different ways to fill the", total_number_of_items, "slots.")

# use permutations to find all the different ways to fill the slots
from itertools import permutations

# create a list to store all the different ways to fill the slots
all_permutations = []

# use permutations to find all the different ways to fill the slots
for permutation in permutations(choices, total_number_of_items):
    all_permutations.append(permutation)

# print all the different ways to fill the slots
for permutation in all_permutations:
    print(permutation)
    

