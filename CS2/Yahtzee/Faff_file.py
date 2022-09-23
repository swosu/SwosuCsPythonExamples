class User_interactions:

    def __init__(self):
        self.data = []
        self.player_count = 0
        self.player_names = []
        self.testing = True

    def testing_or_playing(self):
        user_response = input('1 to play, anything else to test: ')
        if '1' != user_response:
            print('Entering testing mode.')
            self.testing = True
        else:
            print('Welcome to the game.')
            self.testing = False

    def get_player_count(self):
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

    def get_player_names(self):
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
