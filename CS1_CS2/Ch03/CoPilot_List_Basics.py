"""1. Get user inputs: 
Use input() function to gather user inputs like 
my_flower1, 
my_flower2,
my_flower3."""
my_flower1 = input("Enter your first flower: ")
print(f"you entered {my_flower1} for my_flower1")
my_flower2 = input("Enter your second flower: ")
print(f"you entered {my_flower2} for my_flower2")
my_flower3 = input("Enter your third flower: ")
print(f"you entered {my_flower3} for my_flower3")

# 2. Define my_list: Create a list containing my_flower1, my_flower2, and my_flower3.
# Example: Use list syntax [value1, value2, value3]

my_list = [my_flower1, my_flower2, my_flower3]
print(f"your first list called my_list is {my_list}")
# 3. Define your_list: Create a list containing your_flower1 and your_flower2.
your_flower1 = input("Enter your first flower: ")
print(f"you entered {your_flower1} for your_flower1")
your_flower2 = input("Enter your second flower: ")
print(f"you entered {your_flower2} for your_flower2")
your_list = [your_flower1, your_flower2]
print(f"your second list called your_list is {your_list}")
# 4. Define our_list: Concatenate my_list and your_list using the + operator or the extend() method.
our_list = my_list + your_list

# 5. Append their_flower: Use the append() method to add their_flower to the end of our_list.



# 6. Replace my_flower2 with their_flower: You can assign their_flower to the index of my_flower2 in our_list.

# 7. Remove the first occurrence of their_flower: Use the remove() method to delete the first instance of an item.

# 8. Remove the second element of our_list: Use the del statement or pop() method with index 1.

# 9. Print the list at each stage: Use print() function to see the changes after each step.
