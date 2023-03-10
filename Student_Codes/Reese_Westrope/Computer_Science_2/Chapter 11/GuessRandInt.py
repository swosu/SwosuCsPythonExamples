import random
guess = False
correct_num = random.randint(1, 100)


def number_guess(num):
    global guess, correct_num   

    if num == correct_num:
        print("Good job, thats right!")
        guess = True
    elif num < correct_num:
        print("Bad job, that's too low.")
    elif num > correct_num:
        print("Bad job, that's too high.")
    
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    while guess == False:

        user_input = int(input("Guess a number between 1 and 100.\n:"))
        number_guess(user_input)


