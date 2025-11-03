
def get_starting_integer():
    try:
        starting_integer = int(input("Enter the starting integer: "))
        return starting_integer
    except ValueError:
        print("Please enter a valid integer.")
        return get_starting_integer()
    
def get_second_integer():
    while True:
        try:
            second_integer = int(input("Enter the second integer: "))
            return second_integer
        except ValueError:
            print("Please enter a valid integer.")
            continue

def output_the_number_series(starting_integer, second_integer):
    for our_number in range(starting_integer, second_integer + 1, 5):
        print(our_number, end=" ")
    

if __name__ == "__main__":

    print("Hello World!")
    """
    Write a program whose input is two integers. 
    Output the first integer and subsequent increments of 5 as 
    long as the value is less than or equal to the second integer.

    Ex: If the input is:

    -15
    10
    the output is:

    -15 -10 -5 0 5 10 
    """
    # ask the user for the starting integer
    starting_integer = get_starting_integer()
    print("starting integer: ", starting_integer)

    second_integer = get_second_integer()
    print("second integer: ", second_integer)

    # output the number series
    output_the_number_series(starting_integer, second_integer)
