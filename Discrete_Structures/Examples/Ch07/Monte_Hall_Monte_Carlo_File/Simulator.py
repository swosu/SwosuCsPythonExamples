import random

class Simulator:
    def __init__(self):
        self.iteration_count = 0
        self.first_choice = 0
        self.prize_door = 0
        self.door_to_reveal = 0
        self.second_door = 0
        self.decide_to_switch = False
        self.stay_and_win = 0
        self.switch_and_win = 0
        self.swithc_and_lose = 0
        self.stay_and_lose = 0
        self.doors = [1, 2, 3]
        self.options = ['stay', 'switch']

    def single_run(self):
        random.seed(42)
        print('single run')
        self.iteration_count += 1
        self.first_choice = random.choice(self.doors)
        print('first choice:', self.first_choice)
        self.prize_door = random.choice(self.doors)
        print('prize door:', self.prize_door)
        self.get_door_to_reveal()
        print('door to reveal:', self.door_to_reveal)

        if 'switch' == random.choice(self.options):
            self.decide_to_switch = True
        else:
            self.decide_to_switch = False

        self.set_second_choice()

        self.update_results()

        self.print_results()

    def get_door_to_reveal(self):
        print('get door to reveal')
        possible_doors = self.doors.copy()
        possible_doors.remove(self.first_choice)
        if self.prize_door in possible_doors:
            possible_doors.remove(self.prize_door)
        self.door_to_reveal = random.choice(possible_doors)

    def set_second_choice(self):
        print('set second choice')
        if self.decide_to_switch:
            possible_doors = self.doors.copy()
            possible_doors.remove(self.first_choice)
            possible_doors.remove(self.door_to_reveal)
            self.second_door = possible_doors[0]
        else:
            self.second_door = self.first_choice

        print('second door:', self.second_door)




if __name__ == '__main__':
    print('hello')

    test_run = Simulator()

    test_run.single_run()