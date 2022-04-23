"""
A pedometer treats walking 1 step as walking 2.5 feet.

//Then, write a main program
//that reads the number of feet walked as an input,
//calls function feet_to_steps() with the input as an argument,
and outputs the number of steps.

Define a function named feet_to_steps
that takes a float as a parameter, representing the number of feet walked, and
returns an integer that represents the number of steps walked.
Use floating-point arithmetic to perform the conversion.

Ex: If the input is:

150.5
the output is:

60
The program must define and call the following function:
def feet_to_steps(user_feet)

Book Starter Code:
"""

# Define your function here
def feet_to_steps(user_feet):
    print('hello world')
    print(f'inside the function you waled {user_feet} feet.')
    user_steps = float(user_feet) / 2.5
    print(f'{user_feet} becomes {user_steps}.')
    return user_steps

if __name__ == '__main__':
    # Type your code here.
    user_feet = input('please tell us how many feet you walked.')

    print(f'you waled {user_feet} feet.')
    user_steps = feet_to_steps(user_feet)

    print(f'after the function call {user_feet} becomes {user_steps}.')
