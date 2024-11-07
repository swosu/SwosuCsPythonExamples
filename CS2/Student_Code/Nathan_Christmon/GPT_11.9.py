import random

class Guess_Number_Game:

    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.number = random.randint(min, max)





if __name__ == "__main__":
    print ("Hello World")

    game = Guess_Number_Game(1, 100)
    print (game.number)

    while True:
        # ask user for input
        guess = int(input("Guess a number between 1 and 100: "))
        # check if guess is correct
        if guess == game.number:
            print ("Correct!")
            break
        # check if guess is too high
        elif guess > game.number:
            print ("Too high!")
        # check if guess is too low
        elif guess < game.number:
            print ("Too low!")
        # if guess is not correct, ask again
        else:
            print ("Invalid input. Try again.")


    print ("Goodbye World")