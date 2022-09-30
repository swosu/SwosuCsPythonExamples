class game_class:


    def __init__(self):
        self.game_name = ''
        self.upper_limit = 100
        self.lower_limit = 0
        self.game_number = 0
        self.user_guess = 0

    def explain_game(self):
        self.game_name = 'guessing game'
        print(' we are going to guess a number')

    def set_up_game(self):
        print(f'we are going to have you pick a number between ')
        print(f'{self.lower_limit} and {self.upper_limit}.')
