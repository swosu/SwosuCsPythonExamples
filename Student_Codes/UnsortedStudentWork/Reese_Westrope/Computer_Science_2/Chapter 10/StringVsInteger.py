

# Split input into 2 parts: name and age
parts = input('Please enter your name and age.\n:').split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = '\nXXX\nA valid age was not entered.\nPlease enter an integer for your age.\nXXX'
    #age = int(parts[1]) + 1
    print(f'{name} {age}')
    
    # Get next line
    parts = input('Please enter your name and age.\n:').split()
    name = parts[0]

