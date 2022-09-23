class User_interactions:

    def __init__(self):
        self.data = []
        self.player_count = 0

    def get_player_count(self):
        player_count = input('hello, how many players would you like?')
        self.player_count = int(player_count)
        if 0 >= self.player_count:
            print('you don\'t want to play.')
        elif 1 == self.player_count:
            print('you want one player ')
        elif 2 <= self.player_count:
            print(f'you want {self.player_count} players.')
        
