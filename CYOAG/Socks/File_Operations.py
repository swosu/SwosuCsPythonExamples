from Player import Player_class
import json

class File_operation_class:
    """Tools for story telling."""
    def __init__(self):
        self.data = []

    def save_character(self,player):
        print('start saving,', end = '')
        print('change data into a list')
        player_data_list = []
        print(player.get_name())
        player_data_list.append(player.get_name())
        with open('player_data.json', 'w') as file_object:
            json.dump(player_data_list, file_object)
            file_object.close()
        print('... done saving.')

    def load_saved_data(self,player):
        print('opening file...', end='')
        with open('player_data.pickle', 'rb') as file_object:
            player = pickle.load(file_object)
            file_object.close()
            print(' done loading')
            print(player)
            #return player
