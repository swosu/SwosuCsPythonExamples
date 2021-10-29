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
   player = tale.load_or_new_player_menu(disk, player)





   tale.show_menu(player,disk)
