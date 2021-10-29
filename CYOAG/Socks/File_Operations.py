from Player import Player_class
import pickle

class File_operation_class:
    """Tools for story telling."""
    def __init__(self):
        self.data = []

    def save_character(self,player):
        print('start saving,', end = '')
        with open('player_data.pickle', 'wb') as file_object:
            pickle.dump(player, file_object, pickle.HIGHEST_PROTOCOL)
            file_object.close()
        print('... done saving.')

    def load_saved_data(self,player):
        print('opening file...', end='')
        with open('player_data.pickle', 'rb') as file_object:
            player = pickle.load(file_object)
            file_object.close()
            print(' done loading')
            return player
