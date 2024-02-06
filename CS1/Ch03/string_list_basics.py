"""
3.12 LAB: List basics
Given the user inputs, complete a program that does the following tasks:

Define a list, 
my_list, containing the user inputs: 
my_flower1, my_flower2, and my_flower3 in the same order.

Define a list, your_list, 
containing the user inputs, your_flower1 and your_flower2, in the same order.

Define a list, our_list, by concatenating my_list and your_list.

Append the user input, their_flower, to the end of our_list.


Replace my_flower2 in our_list with their_flower.

Remove the first occurrence of their_flower from our_list without using index().

Remove the second element of our_list.
Observe the output of each print statement carefully to understand what was done by each task of the program.

Ex: If the input is:

rose
peony
lily
rose
daisy
aster
the output is:

['rose', 'peony', 'lily', 'rose', 'daisy']
['rose', 'peony', 'lily', 'rose', 'daisy', 'aster']
['rose', 'aster', 'lily', 'rose', 'daisy', 'aster']
['rose', 'lily', 'rose', 'daisy', 'aster']
['rose', 'rose', 'daisy', 'aster']
Starter Code:

my_flower1 = input()
my_flower2 = input()
my_flower3 = input()

your_flower1 = input()
your_flower2 = input()

their_flower = input()





# 3. TODO: Define our_list by concatenating my_list and your_list

print(our_list)

# 4. TODO: Append their_flower to the end of our_list

print(our_list)

# 5. TODO: Replace my_flower2 in our_list with their_flower

print(our_list)

# 6. TODO: Remove the first occurrence of their_flower from
# our_list without using index()

print(our_list)

# 7. TODO: Remove the second element of our_list

print(our_list)

 
"""

# define a list called my_list
my_list = []
print('now the list is: ', my_list)

# 1. TODO: Define my_list containing my_flower1, my_flower2, and my_flower3
# in that order

my_flower1 = input('please input the first flower: ')
print(' you entered the flower: ', my_flower1) 

my_list.append(my_flower1)

print('now the list is: ', my_list)

my_flower2 = input('please input the second flower: ')
print(' you entered the flower: ', my_flower2)

my_list.append(my_flower2)
print('now the list is: ', my_list)

my_flower3 = input('please input the third flower: ')
print(' you entered the flower: ', my_flower3)

my_list.append(my_flower3)
print('now the list is: ', my_list)



# 2. TODO: Define your_list containing your_flower1 and your_flower2
# in that order

your_list = []
print('now the list is: ', your_list)

your_flower1 = input('please input the first flower: ')
print(' you entered the flower: ', your_flower1)

your_list.append(your_flower1)


