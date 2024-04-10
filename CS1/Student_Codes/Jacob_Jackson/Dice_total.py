import random

class GVDie:
    def __init__(self):
        self.my_value = random.randint(1,6)
        self.rand = random.Random()

    def roll(self):
        self.my_value = self.rand.randint(1,6)

    def set_seed(self, seed):
        self.rand.seed(seed)

    def compare_to(self, other):
        return self.my_value - d.my_value
    
    def roll_specific_times(self, die, rolls):
        total = 0
        for i in range(rolls):
            die.roll()
            total += die.my_value
        return total
    
    def reroll_until_fixed_value(die, value):
        rolls = 0
        while True:
            die.roll()
            rolls += 1
            if die.my_value == value:
                return rolls
    
    
    def do_stuff(self, value, count):
        rolls = 0
        hits = 0
        while (True):
            result = random.randint(1,6)
            rolls += 1
            if value == result:
                hits += 1
            if hits >= count:
                return rolls

if __name__ == "__main__":
    goal_value = 6
    goal_count = 3
    die = GVDie()
    die.set_seed(15)
    count = die.do_stuff(goal_value, goal_count)
    rolls = int(input("How many times do you want to roll the die? "))
    total = die.roll_specific_times(die, rolls)
    print(f"{rolls} rolls return a total of {total}")

