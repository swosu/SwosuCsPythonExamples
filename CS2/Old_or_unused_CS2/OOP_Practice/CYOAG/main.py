from character_class_file import character
from game_class_file import game

if __name__ == '__main__':

    player_1 = character()
    player_1.set_name('Bob')
    print(f'our health is {player_1.get_health()}.')

    player_1.take_damage(9)
    print(f' after damage our health is {player_1.get_health()}.')

    print('We see a drop item.')
    print('We pick up a potion')
    player_1.set_health(10)
    print(f' after potion our health is {player_1.get_health()}.')
