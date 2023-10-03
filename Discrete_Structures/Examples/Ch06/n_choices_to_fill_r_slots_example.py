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

# working from a website: 
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-52.php

from itertools import product

def all_repeats(chioces, total_number_of_items):
    results = []
    for individual_option in product(choices, repeat=total_number_of_items):
        results.append(individual_option)
    return results

# print the option number and all options
print('if order matters, here is the full list.')
option_number = 1
list_of_all_options_with_repeats = all_repeats(choices, total_number_of_items)
for option in list_of_all_options_with_repeats:
    print(option_number, option)
    option_number += 1

# repeat the process if order does not matter
print('if order does not matter, here is the full list.')

# go through the list of all options with repeats and sort each option alphabetically
list_of_all_options_without_repeats = []
for option in list_of_all_options_with_repeats:
    option = sorted(option)
    list_of_all_options_without_repeats.append(option)

# remove duplicates
list_of_all_options_without_repeats = list(set(tuple(x) for x in list_of_all_options_without_repeats))

# print the option number and all options
option_number = 1
for option in list_of_all_options_without_repeats:
    print(option_number, option)
    option_number += 1
    

    

