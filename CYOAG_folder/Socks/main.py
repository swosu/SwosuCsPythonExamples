from Story import Story_class
from Player import Player_class
from File_Operations import File_operation_class

if __name__ == "__main__":
   print('let it begin!')

   # creating objects
   tale = Story_class()
   player = Player_class()
   disk = File_operation_class()

   tale.print_start()
   tale.create_player(player)

   print('checking, you said,', player.get_name())

   disk.save_character(player)


   #player = tale.load_or_new_player_menu(disk, player)

   #tale.show_menu(player,disk)
