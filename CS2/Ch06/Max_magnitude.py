"""
23.2 LAB: Max magnitude
Write a function max_magnitude() with three integer parameters that returns the largest magnitude value. Use the function in the main program that takes three integer inputs and outputs the largest magnitude value.

Ex: If the inputs are:

5
7
9
function max_magnitude() returns and the main program outputs:

9
Ex: If the inputs are:

-17
-8
-2
function max_magnitude() returns and the main program outputs:

-17
Note: The function does not just return the largest value, which for -17 -8 -2 would be -2. Though not necessary, you may use the built-in absolute value function to determine the max magnitude, but you must still output the input number (Ex: Output -17, not 17).

Your program must define and call the following function:
def max_magnitude(user_val1, user_val2, user_val3)

Starter Code


"""
# Define your function here.

def max_magnitude(num_1, num_2, num_3): 
    #print('stuff')
    if abs(num_1) > abs(num_2):
        #print(f'{num_1} is bigger than {num_2}')
        if abs(num_1) > abs(num_3):
            return num_1
        else:
            return num_3
    else:
        if abs(num_3) > abs(num_2):
            return num_3
        else:
            return num_2

if __name__ == '__main__':
    # Type your code here.
    #print('hello from inside the code.')
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    max_number = max_magnitude(num_1, num_2, num_3)
    #print(f' our max number is: {max_number}.')
    print(max_number)
