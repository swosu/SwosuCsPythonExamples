from Story import Story_class
from Player import Player_class

if __name__ == "__main__":
   print('let it begin!')

   tale = Story_class()
   tale.print_start()

   player = Player_class()
   tale.create_player(player)
