"""
Write a code to have the user input numbers. 
Seperate numbers with a space.
Press enter when they are done.
Pass the numbers to the function.
The function should return the largest magnitude value.
This should be the absolute value of the largest magnitude.
"""



if __name__ == "__main__":
    print('hello')

    # Get user input
    user_input = input('Enter numbers seperated by a space. Press enter when complete: ')
    # Split the input into a list
    user_input = user_input.split()
    # Convert the list to integers
    user_input = [abs(int(i)) for i in user_input]
    # Sort the list
    user_input.sort()
    # Get the last item in the list
    max_magnitude = user_input[-1]
    # Get the absolute value of the last item in the list
    max_magnitude = abs(max_magnitude)
    # Print the absolute value of the last item in the list
    print(f'The largest magnitude value is {max_magnitude}.')
