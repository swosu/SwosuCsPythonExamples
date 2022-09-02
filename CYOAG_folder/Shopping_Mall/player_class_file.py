class player_class:


    def __init__(self):
        self.player_name = ''

    def get_player_name(self):
        print('Hello player!')
        self.player_name = input('please enter your name: ')

    def greet_player(self):
        print(f'It is nice to meet you, {self.player_name}.')
