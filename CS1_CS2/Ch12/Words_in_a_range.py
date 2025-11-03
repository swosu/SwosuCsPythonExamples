import os



if __name__ == '__main__':

    """Write a program that first reads in the name of an input file, 
    followed by two strings representing the lower and upper bounds of a search range. 
    The file should be read using the file.readlines() method. 
    The input file contains a list of alphabetical, 
    ten-letter strings, each on a separate line. 
    Your program should determine if the strings from the 
    list are within that range (inclusive of the bounds) 
    and output the results."""

    # print flie name availible in the current directory
    print("Files in the current directory: ")
    print(os.listdir())

    # Get the file name
    file_name = input("Enter the file name: ")
    print('you entered: ', file_name)

    # Get the lower bound
    lower_bound = input("Enter the lower bound: ")
    print('you entered: ', lower_bound)

    # Get the upper bound
    upper_bound = input("Enter the upper bound: ")
    print('you entered: ', upper_bound)

    # Open the file using file.readlines()
    print('Opening the file: ', file_name)
    with open(file_name, 'r') as file:
        words = file.readlines()
        print(words)

    # Loop through the list of words
    for word in words:
        # Strip the new line character
        word = word.strip()

        # Check if the word is within the range
        if lower_bound <= word <= upper_bound:
            print(f'{word} - in range')
        else:
            print(f'{word} - not in range')

    # Close the file
    file.close()


