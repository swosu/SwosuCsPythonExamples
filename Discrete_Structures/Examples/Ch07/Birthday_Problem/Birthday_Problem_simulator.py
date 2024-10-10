import random

class Birthday_problem_simulator():
    def __init__(self):
        self.number_of_people = 1
        self.number_of_rooms = 1
        self.person_birthday = 0
        self.list_of_birthdays = []
        self.set_of_birthdays = None
        self.had_duplicates = False
        self.duplicate_count = 0
        self.percentage = 0
        self.no_match_probability = 1.0

    def set_number_of_people(self, number_of_people):
        self.number_of_people = number_of_people
        
    
    def generate_birthdays(self):
        for person in range(self.number_of_people):
            self.person_birthday = random.randint(1, 366)
            self.list_of_birthdays.append(self.person_birthday)

    def check_for_duplicates(self):
        self.set_of_birthdays = set(self.list_of_birthdays)
        if len(self.set_of_birthdays) < len(self.list_of_birthdays):
            print(f"Duplicate birthdays found in the list of birthdays: {self.list_of_birthdays}")
            self.had_duplicates = True
        else:
            print("No duplicate birthdays found in the list of birthdays.")
            self.had_duplicates = False

    def print_results(self):
        if self.had_duplicates:
            print("There were duplicate birthdays found.")
        else:
            print("There were no duplicate birthdays found.")

    def print_batch_results(self):
        print(f"Number of rooms: {self.number_of_rooms}")
        print(f"Number of duplicate birthdays found: {self.duplicate_count}")

    def set_number_of_rooms(self, number_of_rooms):
        self.number_of_rooms = number_of_rooms

    def update_duplicate_count(self):
        if self.had_duplicates:
            self.duplicate_count += 1

    def run_simulation(self):
        for room in range(self.number_of_rooms):
            self.generate_birthdays()
            self.check_for_duplicates()
            self.update_duplicate_count()
            self.print_results()
            self.list_of_birthdays.clear()
        
        self.print_results()

    def set_chosen_percentage(self, percentage):
        self.percentage = percentage

    def set_find_amount_of_people(self):
        self.no_match_probability = 1.0
        self.number_of_people = 0

        while self.no_match_probability > (1 - self.percentage/100):
            self.number_of_people += 1
            self.no_match_probability *= (365 - self.number_of_people) / 365

        print(f"Number of people needed to have a {self.percentage}% chance of having a matching birthday: {self.number_of_people}")

    

    
    

    
        
        
if __name__ == '__main__':
    #test_run = Birthday_problem_simulator()
    #test_run.set_number_of_people(10)
    #test_run.generate_birthdays()
    #print(test_run.list_of_birthdays)
    #test_run.check_for_duplicates()
    #test_run.print_results()

    #test_batch.set_number_of_people(23)
    #test_batch.set_number_of_rooms(10)
    #test_batch.run_simulation()
    #test_batch.print_batch_results()
    
    test_percentage_hunter = Birthday_problem_simulator()
    desired_percentage = int(input("Enter the desired percentage: "))
    test_percentage_hunter.set_chosen_percentage(desired_percentage)
    test_percentage_hunter.set_find_amount_of_people()
    
