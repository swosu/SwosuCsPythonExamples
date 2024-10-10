import random
import time

class Simulator:
    def __init__(self):
        self.iteration_count = 0
        self.first_choice = 0
        self.prize_door = 0
        self.door_to_reveal = 0
        self.second_chioce = 0
        self.decide_to_switch = False
        self.switch_count = 0
        self.stay_and_win = 0
        self.switch_and_win = 0
        self.swithc_and_lose = 0
        self.stay_and_lose = 0
        self.doors = [1, 2, 3, 4]
        self.options = ['stay', 'switch']

    def single_run(self):
        self.iteration_count += 1
        self.first_choice = random.choice(self.doors)
        self.prize_door = random.choice(self.doors)
        self.get_door_to_reveal()

        if 'switch' == random.choice(self.options):
            self.decide_to_switch = True
            self.switch_count += 1
        else:
            self.decide_to_switch = False

        self.set_second_choice()
        self.update_results()
        

    def get_door_to_reveal(self):
        possible_doors = self.doors.copy()
        possible_doors.remove(self.first_choice)
        if self.prize_door in possible_doors:
            possible_doors.remove(self.prize_door)
        self.door_to_reveal = random.choice(possible_doors)

    def set_second_choice(self):
        if self.decide_to_switch:
            possible_doors = self.doors.copy()
            possible_doors.remove(self.first_choice)
            possible_doors.remove(self.door_to_reveal)
            self.second_chioce = random.choice(possible_doors)
        else:
            self.second_chioce = self.first_choice

    def update_results(self):
        if self.prize_door == self.second_chioce:
            if self.decide_to_switch:
                self.switch_and_win += 1
            else:
                self.stay_and_win += 1
        else:
            if self.decide_to_switch:
                self.swithc_and_lose += 1
            else:
                self.stay_and_lose += 1

    def print_single_round_results(self):

        door_selection_story = f"First choice: {self.first_choice}, Prize door: {self.prize_door}, Door to reveal: {self.door_to_reveal}, Second choice: {self.second_chioce}, Decide to switch: {self.decide_to_switch}"
        results_from_chioces = f"Stay and win: {self.stay_and_win}, Switch and win: {self.switch_and_win}, Switch and lose: {self.swithc_and_lose}, Stay and lose: {self.stay_and_lose}"
        print(door_selection_story)
        print(results_from_chioces)

    def set_seed(self, seed):
        random.seed(seed)

    def print_batch_results(self):
        print(f'Number of iterations: {self.iteration_count}')
        print(f'Number of times switched: {self.switch_count}')
        print(f'switch percentage: {100 * self.switch_count / self.iteration_count}%')
        print(f'Number of times stayed and won: {self.stay_and_win}')
        print(f'Number of times switched and won: {self.switch_and_win}')
        print(f'Number of times switched and lost: {self.swithc_and_lose}')
        print(f'Number of times stayed and lost: {self.stay_and_lose}')
        print(f'win percentage: {100 * (self.stay_and_win + self.switch_and_win) / self.iteration_count}%')
        print(f'lose percentage: {100 * (self.stay_and_lose + self.swithc_and_lose) / self.iteration_count}%')
        print(f'stay win percentage: {100 * self.stay_and_win / self.iteration_count}%')
        print(f'switch win percentage: {100 * self.switch_and_win / self.iteration_count}%')
        

if __name__ == '__main__':
    """
    test_run = Simulator()
    test_run.set_seed(42)
    for run_count in range(10):
        print(f'Run number: {run_count + 1}')
        test_run.single_run()
        test_run.print_single_round_results()

    test_run.print_batch_results() 
    """
    
    start_time = time.time()
    larger_run = Simulator()
    larger_run.set_seed(42)
    #larger_run.set_seed(time.time())
    number_of_runs = 1000000
    for run_count in range(number_of_runs):
        larger_run.single_run()
    
    stop_time = time.time()
    larger_run.print_batch_results()
    print(f'Time taken: {stop_time - start_time} seconds')
    
    