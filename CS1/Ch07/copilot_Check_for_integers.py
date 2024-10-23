"""
https://github.com/swosu/SwosuCsPythonExamples
Forms often allow a user to enter an integer. 
Write a program that takes in a string representing an integer as input, 
and outputs Yes if every character is a digit 0-9 or No otherwise.

Ex: If the input is:

1995
the output is:

Yes
Ex: If the input is:

42,000
or any string with a non-integer character, the output is:

No
"""

def get_user_input():
    print("Enter a string representing an integer: ")
    print('Enter "q" to quit')
    user_input = input()
    return user_input
    
def check_for_integers(user_input):
    if user_input.isdigit():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':

    user_input = get_user_input()
    print(f"our user input is: {user_input}")

    check_for_integers(user_input)