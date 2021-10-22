import random
print('You wake up in the forest.')
print('You are hungry.')
print('you have 3 days of food.')
print('a single great fish can feed you for 3 days.')
print('You need to catch a fish to win.')


have_honey = False
keep_game_going = True

def winner():
    print('you have caught a fish!')
    keep_game_going = False
    return keep_game_going

def go_fishing_no_honey(random_number):
    print('so here we are, fishing with no honey.')
    keep_game_going = True
    if 0.60 <= random_number:
        keep_game_going = winner()
    else:
        print('you did not catch a fish.')
        print('you did not have any honey.')
    return keep_game_going

def go_fishing(have_honey):
    keep_game_going = True
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
                keep_game_going = winner()
            else:
                go_fishing(have_honey)
        if choice == n:
            go_fishing_no_honey(random_number)
    else:
        print('you are going to try to fish without honey.')
        keep_game_going = go_fishing_no_honey(random_number)
    return keep_game_going


user_agreement = input('would you like to keep playing? (y/n)\n')
if 'n' == user_agreement:
    print('so long and thank you for stopping.')
    keep_game_going = False
else:
    print('we will keep playing.')
while keep_game_going:

    keep_game_going = go_fishing(have_honey)
    user_agreement = input('would you like to keep playing? (y/n)\n')
    if 'n' == user_agreement:
        print('so long and thank you for stopping.')
        keep_game_going = False
    else:
        print('we will keep playing.')
