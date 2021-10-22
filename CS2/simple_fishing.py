
def print_welcome():
    print('this is the fishing game.')
    print('you need to catch a fish to win.')

def simple_game():
    keep_fishing = True
    have_honey = False
    while keep_fishing:
        user_choice = int(input('Please make a choice: \n 1 to fish, 2 to get honey, 3 quit\n'))

        if 1 == user_choice:
            print('lets try to catch something')
        elif 2 == user_choice:
            print('lets go get some honey')
        elif 3 == user_choice:
            keep_fishing = False
            print('this ends our fishing trip.')

def go_fishing():
    print('here we are, fishing!')
    print_welcome()
    simple_game()
