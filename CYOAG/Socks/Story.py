from Player import Player_class

class Story_class:
    """Tools for story telling."""
    def __init__(self):
        self.data = []

    def print_start(self):
        print('Hello there strong one.')
        print('It is another glorious day!')
        print('Any day as you is a glorious day. Just look at those scales.')
        print('You my friend ara a dragonborn.')
        print('Quick on your feet, strong, and oh so funny...')

    def create_player(self, player):
        your_name = input('What is your name?')
        player.set_name(your_name)
        print('it is nice to meet you,', player.get_name(), '.')
