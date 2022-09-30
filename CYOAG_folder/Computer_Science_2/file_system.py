class file_system:
   def __init__(self):
       self.data = []
       
       
   def save_name(self, player_data):
       with open('player_data.txt', 'w') as f:
           f.write(player_data)

