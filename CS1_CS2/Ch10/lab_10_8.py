# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except:
        age = 0
    print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]
