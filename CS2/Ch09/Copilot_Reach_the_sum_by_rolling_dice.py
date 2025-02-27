import random

class Crappy_Dice_Class():
    def __init__(self):
        self.desired_total = 0
        self.current_roll = 0
        self.current_total = 0
        self.number_of_rolls = 0

    def set_random_seed(self):
        try:
            seed = int(input("Enter a seed: "))
            random.seed(seed)
        except ValueError:
            print("Enter a valid number")
            self.set_random_seed()
        

    def get_desired_total(self):
        try:
            self.desired_total = int(input("Enter the desired total: "))
            if self.desired_total < 2 or self.desired_total > 1000:
                print("Enter a valid number between 2 and 1000")
                self.get_desired_total()
        except ValueError:
            print("Enter a valid number between 2 and 12")
            self.get_desired_total()

    def roll_dice(self):
        self.current_roll = random.randint(1, 6)

    def play_game(self):
        while self.current_total < self.desired_total:
            self.roll_dice()
            self.current_total += self.current_roll
            self.number_of_rolls += 1
            print(f"Roll: {self.current_roll}, Total: {self.current_total}")
        print(f"Got to {self.desired_total} in {self.number_of_rolls} rolls")


if __name__ == "__main__":

    object = Crappy_Dice_Class()
    object.set_random_seed()
    object.get_desired_total()
    object.play_game()

    other_object = Crappy_Dice_Class()
    other_object.set_random_seed()
    other_object.get_desired_total()
    other_object.play_game()



