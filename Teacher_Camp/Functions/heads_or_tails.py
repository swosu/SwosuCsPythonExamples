def greet_user():
    print('Welcome to our heads or tails game!')

def get_user_selection():
    # Get user selection
    user_selection = \
    input('please press 1 for heads or 2 for tails and then press enter')

    if str(1) == user_selection:
        print('you selected heads')
    elif str(2) == user_selection:
        print('you selected tails')
    else:
        print("you didn't follow instructions...")
        user_selection = \
        input('please press 1 for heads or 2 for tails and then press enter')
    return user_selection

def get_flip_result():
    # get flip result
    from random import random
    random_number = random()
    if 0.5 <= random_number:
        print(f'{random_number:.3f} is greater than or equal to 0.5.')
        flip_result = "1"
    else:
        print(f'{random_number:.3f} is less than 0.5.')
        flip_result = "2"

    if str(1) == flip_result:
        print('computer selected heads')
    elif str(2) == flip_result:
        print('computer selected tails')

    return flip_result


def evaluate_results(user_selection, flip_result):
    if flip_result == user_selection:
        print("The user is the winner!")
    else:
        print("The computer did not guess correctly.")



if __name__ == '__main__':
    print('welcome to functions')
    greet_user()
    user_selection = get_user_selection()
    flip_result = get_flip_result()
    evaluate_results(user_selection, flip_result)
