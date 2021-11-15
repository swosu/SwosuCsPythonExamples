from Player import Player_class
from File_Operations import File_operation_class

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

    def load_or_new_player_menu(self, disk, player):
        print('press 1 to load a saved game.')
        print('press 2 to create a new player.')
        user_choice = int(input())

        if 1 == user_choice:
            print('begin loading...', end='')
            player = disk.load_saved_data(player)
            print('it is nice to meet you,', player.get_name(), '.')
        elif 2 == user_choice:
            self.create_player(player)
            #return player
        else:
            self.load_or_new_player_menu()


    def create_player(self, player):
        your_name = input('What is your name?')
        player.set_name(your_name)
        print('it is nice to meet you,', player.get_name(), '.')

    def show_menu(self, player, disk):
        print('you are playing as', player.get_name())
        print('press q to quit.')
        print('press s to save.')
        print('press m for menu.')
        user_choice = input().lower()
        if 's' == user_choice:
            disk.save_character(player)
            self.show_menu(player, disk)
        elif 'm' == user_choice:
            self.show_menu(player, disk)
        else:
            print('so long and thanks for playing.')
