import random

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 6, 8, 10, 12]
list3 = [3, 6, 9, 12, 15, 18]
list4 = [4, 8, 12, 16, 20, 24]

def choose_list():
    chosen_list = random.choice([list1, list2, list3, list4])
    print(chosen_list[0:5])
    return chosen_list

chosen_list = choose_list()
user_input = int(input("What's the next number in the sequence? "))
if user_input == chosen_list[-1]:
    print("Correct!")
else:
    print("Incorrect!")
