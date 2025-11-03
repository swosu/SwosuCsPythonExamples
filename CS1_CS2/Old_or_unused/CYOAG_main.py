import simple_fishing
print('hello.')
print('welcome to our CYOAG main game.')

keep_going = True

while keep_going:
    user_choice = int(input('please make a choice. 1 to quit. 2 to fish.\n'))

    if 1 == user_choice:
        print('so long and thanks for all the fish...');
        keep_going = False
    elif 2 == user_choice:
        print('lets go fishing!')
        simple_fishing.go_fishing()
    else:
        print('you did not make a good choice')
