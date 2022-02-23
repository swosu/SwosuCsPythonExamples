
import player_class_file
import game_class_file

if __name__ == "__main__":

    print('Hello')

    player_obj = player_class_file.player_class()
    game_obj = game_class_file.game_class()

    player_obj.get_player_name()

    player_obj.greet_player()

    game_obj.explain_game()

    game_obj.set_up_game()
