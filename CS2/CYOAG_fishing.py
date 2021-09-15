import random
print('You wake up in the forest.')
print('You are hungry.')
print('You need to catch a fish to win.')

have_honey = False

def winner():
    print('you have caught a fish!')

def go_fishing_no_honey(random_number):
    if 0.60 <= random_number:
        winner()
    else:
        go_fishing(have_honey)

def go_fishing(have_honey):
    print('you have decided to go fishing.')
    random_number = random.random()
    print('our random number was:' + \
        str(random_number))
    if have_honey:
        choice = \
        input('would you like to use your honey? (y/n)\n')
        if choice == y:
            have_honey = False
            if 0.75 >= random_number:
                winner()
            else:
                go_fishing(have_honey)
        if choice == n:
            go_fishing_no_honey(random_number)
    else:
        go_fishing_no_honey(random_number)


go_fishing(have_honey)
