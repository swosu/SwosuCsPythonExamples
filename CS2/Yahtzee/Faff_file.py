class User_interactions:


    def __init__(self):
        self.data = []
        self.player_count = 0
        self.player_names = []
        self.testing = True
        self.dice_on_table = [1, 2, 3, 4, 5]
        self.roll_count = 0

    def testing_or_playing(self):
        user_response = input('1 to play, anything else to test: ')
        if '1' != user_response:
            print('Entering testing mode.')
            self.testing = True
        else:
            print('Welcome to the game.')
            self.testing = False

    def ask_player_what_to_keep(self):
        if self.testing:
            print('stuck here.')
        else:
            print('still stuck here.')
    def ask_player_count(self):
        if self.testing:
            player_count = 3
        else:
            player_count = input('hello, how many players would you like?')

        self.player_count = int(player_count)
        if 0 >= self.player_count:
            print('you don\'t want to play.')
        elif 1 == self.player_count:
            print('you want one player ')
        elif 2 <= self.player_count:
            print(f'you want {self.player_count} players.')

    def get_player_count(self):
        return self.player_count

    def ask_player_names(self):
        if self.testing:
            self.player_names.append('bob')
            self.player_names.append('susan')
            self.player_names.append('link')
        else:
            for item in range(0,self.player_count):
                name = input(f'Player {item+1}, please enter your name: ')
                self.player_names.append(name)

        print('for this game, we have the following player:')
        print(self.player_names)

    def get_player_name(self, player_number):
        return self.player_names[player_number]


    def roll_new_five(self):
        import random
        self.roll_count = 1
        print('New roll.')
        for die in range(0, len(self.dice_on_table)):
            self.dice_on_table[die] = random.randint(1,6)
        print('here are the dice on the table.\nDICE NUMBER')
        print('\t1\t2\t3\t4\t5\nDICE VALUE')
        print(f'\t{self.dice_on_table[0]}')
