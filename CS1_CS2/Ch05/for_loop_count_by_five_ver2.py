'''version 1
our_number_start = -15 #int(input('Enter a number where you want to start counting: '))
our_number_stop = 10
while our_number_start <= our_number_stop:
  print('our number is now: ', our_number_start)
  #our_number += 1
  our_number_start = our_number_start + 5

print('we are outside of the loop.')
'''

# version 2
'''
our_number_start = -15
our_number_stop = 10
while True:
    print('our number is now: ', our_number_start)
    our_number_start = our_number_start + 5
    if our_number_start > our_number_stop:
        break

print('we are outside of the loop.')
'''

# version 3
'''
our_number_start = -15
our_number_stop = 10
end_of_loop_step_size = 5
for index in range(our_number_start, our_number_stop + 1, end_of_loop_step_size):
    print('our number is now: ', index)
'''

'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print('i is ', i, " which is no longer less than 6")
'''

'''
print('our fruit is: ', end='')
fruits = ["apple", "banana", "soda", "orange", "kiwi", "melon", "mango", 7]
for our_fruit in fruits:
  
  print(our_fruit, end=', ')

print('we are outside of the loop.')
print('our list is: ', fruits)
'''

'''
for x in range(6):
  print(x)
'''

'''
for x in range(2, 6):
  print(x)
'''

'''
for x in range(2, 30, 3):
  print(x)

'''

'''
start = -15
stop = 10
step_size = 5
for our_number in range (start, stop + 1, step_size):
    print('our number is now: ', our_number)

'''

#problem 2
#Numerous engineering and scientific applications require finding 
# solutions to a set of equations. 
# Ex: 8x + 7y = 38 
# and 3x - 5y = -1 
# have a solution x = 3, y = 2.
#  Given integer coefficients of two linear equations with 
# variables x and y, use brute force to find an integer solution 
# for x and y in the range -10 to 10.

# Hint: use a for loop and an if statement to brute force check all

# possible values of x and y in the range -10 to 10.

# Hint: use a for loop and an if statement to brute force check all

for x_guess in range(-10, 11):
    for y_guess in range(-10, 11):
        print('x is: ', x_guess, 'y is: ', y_guess, end = ' ')
        equation1 = 8*x_guess + 7*y_guess
        if 38 == equation1:
            print('equation1 is a match.')
        equation2 = 3*x_guess - 5*y_guess
        if -1 == equation2:
            print('equation2 is a match.')
        print('equation1 is: ', equation1, ', equation2 is: ', equation2)
        if 8*x_guess + 7*y_guess == 38 and 3*x_guess - 5*y_guess == -1:
            print('\n\nsolution found')
            print('x is: ', x_guess, ', y is: ', y_guess)
            break
    else:
        print('no solution found')
        continue
    break