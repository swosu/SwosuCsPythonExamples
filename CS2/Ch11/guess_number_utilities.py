import random

def greetUser():
    print('hello user.')

def generate_random_number():
    random.seed(900)
    our_random_number = random.randint(1,101)
    return our_random_number

def get_user_guess():
    user_guess = input('please enter your guess between 1 and 100\n')
    #TODO: need to add some limits on what we let pass
    return user_guess

def was_answer_correct(our_random_number,user_guess):
    if(int(our_random_number) == int(user_guess)):
        user_was_wrong = False
        print('you were correct.')
        return user_was_wrong
    else:
        print('you were not correct.')
        user_was_wrong = True
        return user_was_wrong

def give_user_a_hint(our_random_number,user_guess):
    if(int(our_random_number) > int(user_guess)):
        print('too low')
    else:
        print('too high')
