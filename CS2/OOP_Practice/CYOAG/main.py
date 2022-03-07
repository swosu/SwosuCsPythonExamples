from character_class_file import character

if __name__ == '__main__':

    our_character_object = character()
    print(f'our health is {our_character_object.get_health()}.')

    our_character_object.take_damage(9)
    print(f' after damage our health is {our_character_object.get_health()}.')

    print('We see a drop item.')
    print('We pick up a potion')
    our_character_object.set_health(10)
    print(f' after potion our health is {our_character_object.get_health()}.')
