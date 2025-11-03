# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    #        Insert try/except blocks to catch the exception.
    #        If the exception occurs, print "Invalid age" and continue to the next line.
    try:
        age = int(parts[1]) + 1
        print(f'{name} {age}')
    except:
        print('Invalid age')
        age = 0

    
    # Get next line
    parts = input().split()
    name = parts[0]