

if __name__ == '__main__':
    print('hello.')

    """
    The given program reads a list of single-word
    first names and ages (ending with -1),
    and outputs that list with the age incremented.

    The program fails and throws an exception if
        the second input on a line is a string rather
        than an integer.

    At FIXME in the code,
    add try and except blocks to catch the
    ValueError exception and output 0 for the age.
    """

    # Split input into 2 parts: name and age
    parts = input("please give a name and a age\n").split()
    name = parts[0]
    while name != '-1':
        # FIXME: The following line will throw ValueError exception.
        #        Insert try/except blocks to catch the exception.
        try:
            age = int(parts[1]) + 1
            print(f'your name was {name}, and next year you will be {age}')
        except:
            print(f'problem for{name}, age is reset to: {0}')
        # Get next line
        parts = input("please give another name and a age\n").split()
        name = parts[0]
