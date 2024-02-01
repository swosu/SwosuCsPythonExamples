from random import shuffle

"""
Scrabble Game
Classes:
Tile - keeps track of the tile letter and value
Rack - keeps track of the tiles in a player's letter rack
Bag - keeps track of the remaining tiles in the bag
Word - checks the validity of a word and its placement
Board - keeps track of the tiles' location on the board
"""

tile_dict = { 
    'A': 1,
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10, 
    '#': 0 

    }    

class Tile:

    def __init__(self, letter, letter_values):

        self.letter = letter.upper()
        if self.letter in letter_values.keys():
            self.score = letter_values[self.letter]
        else:
            self.score = 0
        
    def GetTile(self):
        return self.letter

    def GetScore(self):
        return self.score

class Bag:

    def __init__(self):
        self.bag = []
        self.initialize_bag()

        
    def AddBagTile(self, tile, quantity):
        for number in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        global tile_dict
        self.AddBagTile(Tile('B', tile_dict), 2)
        self.AddBagTile(Tile('A', tile_dict), 9)
        self.AddBagTile(Tile('C', tile_dict), 2)
        self.AddBagTile(Tile('D', tile_dict), 4)
        self.AddBagTile(Tile('E', tile_dict), 12)
        self.AddBagTile(Tile('F', tile_dict), 2)
        self.AddBagTile(Tile('G', tile_dict), 3)
        self.AddBagTile(Tile('H', tile_dict), 2)
        self.AddBagTile(Tile('I', tile_dict), 9)
        self.AddBagTile(Tile('J', tile_dict), 9)
        self.AddBagTile(Tile('K', tile_dict), 1)
        self.AddBagTile(Tile('L', tile_dict), 4)
        self.AddBagTile(Tile('M', tile_dict), 2)
        self.AddBagTile(Tile('N', tile_dict), 6)
        self.AddBagTile(Tile('O', tile_dict), 8)
        self.AddBagTile(Tile('P', tile_dict), 2)
        self.AddBagTile(Tile('Q', tile_dict), 1)
        self.AddBagTile(Tile('R', tile_dict), 6)
        self.AddBagTile(Tile('S', tile_dict), 4)
        self.AddBagTile(Tile('T', tile_dict), 6)
        self.AddBagTile(Tile('U', tile_dict), 4)
        self.AddBagTile(Tile('V', tile_dict), 2)
        self.AddBagTile(Tile('W', tile_dict), 2)
        self.AddBagTile(Tile('X', tile_dict), 1)
        self.AddBagTile(Tile('Y', tile_dict), 2)
        self.AddBagTile(Tile('Z', tile_dict), 1)
        self.AddBagTile(Tile('#', tile_dict), 2)
        shuffle(self.bag)
        
    def TakeBagTile(self):
        return self.bag.pop()

    def GetRemainingTiles(self):
        return len(self.bag)

class Rack:

    def __init__(self, bag):
        self.rack = []
        self.bag = bag
        self.InitializeRack()     

    def InitializeRack(self):
        for tile in range(7):
            self.AddToRack()
                
    def AddToRack(self):
        self.rack.append(self.bag.TakeBagTile())

    def GetRackLength(self):
        return len(self.rack)

    def GetRackStr(self):
        return ", ".join(str(item.GetTile()) for item in self.rack)


    def GetRackArray(self):
        return self.rack


    def TakeRackTile(self, tile):
        self.rack.remove(tile)

    #def GetRackLength(self):
        #return len(self.rack)

    def RefillRack(self):
        while len(self.rack) < 7 and self.bag.GetRemainingTiles() > 0:
            self.rack.append(self.bag.TakeBagTile())
            
class Player:

    def __init__(self, bag):
        self.name = ""
        self.rack = Rack(bag)
        self.score = 0

    def SetName(self, name):
        self.name = name

    def GetName(self):
        return self.name
        
    def GetRack(self):
        return self.rack.GetRackStr()

    def GetRackArr(self):
        return self.rack.GetRackArray()
        
        
    def IncreaseScore(self, increase):
        self.score += increase
        return self.score
        
    def GetScore(self):
        return self.score

class Board:

    def __init__(self):
        self.board = [["   " for space in range(15)] for other_space in range(15)]
        self.AddSpecialSpaces()
        self.board[7][7] = " * "

    def GetBoardStr(self):
        board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        board = list(self.board)
        for i in range(len(board)):
            if i < 10:
                board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
            if i >= 10:
                board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        return board_str

    def AddSpecialSpaces(self):
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for coordinate in TRIPLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TWS"
        for coordinate in TRIPLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TLS"
        for coordinate in DOUBLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DWS"
        for coordinate in DOUBLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DLS"

    def PlaceWord(self, word, location, direction, player):
        global premium_spots
        premium_spots = []
        direction = direction.lower()
        word = word.upper()

        if direction.lower() == "right":
            for letter in range(len(word)):
                if self.board[location[0]][location[1]+letter] != "   ":
                    premium_spots.append((word[letter], self.board[location[0]][location[1]+letter]))
                self.board[location[0]][location[1]+letter] = " " + word[letter] + " "

        elif direction.lower() == "down":
            for letter in range(len(word)):
                if self.board[location[0]][location[1]+letter] != "   ":
                    premium_spots.append((word[letter], self.board[location[0]][location[1]+letter]))
                self.board[location[0]+letter][location[1]] = " " + word[letter] + " "

        for letter in word:
            for tile in player.GetRackArr():
                if tile.GetTile() == letter:
                    player.rack.TakeRackTile(tile)
        player.rack.RefillRack()

    def GetBoardArr(self):
        return self.board

class Word:
    def __init__(self, word, location, player, direction, board):
        self.word = word.upper()
        self.location = location
        self.player = player
        self.direction = direction.lower()
        self.board = board

    def CheckWord(self):
        global round_number, players
        word_score = 0
        global dictionary 
        if "dictionary" not in globals():
            dictionary = open("dic.txt").read().splitlines()

        current_board_ltr = ""
        needed_tiles = ""
        blank_tile_val = ""   

        if self.word != "":

            if "#" in self.word:
                while len(blank_tile_val) != 1:
                    blank_tile_val = input("Please enter the letter value of the blank tile: ")
                self.word = self.word[:Word.index("#")] + blank_tile_val.upper() + self.word[(Word.index("#")+1):]

            if self.direction == "right":
                for space in range(len(self.word)):
                    if self.board[self.location[0]][self.location[1]+space][1] == " " or self.board[self.location[0]][self.location[1]+space] == "TLS" or self.board[self.location[0]][self.location[1]+space] == "TWS" or self.board[self.location[0]][self.location[1]+space] == "DLS" or self.board[self.location[0]][self.location[1]+space] == "DWS" or self.board[self.location[0]][self.location[1]+space][1] == "*":
                        current_board_ltr += " "
                    else:
                        current_board_ltr += self.board[self.location[0]][self.location[1]+space][1]
            elif self.direction == "down":
                for space in range(len(self.word)):
                    if self.board[self.location[0]+space][self.location[1]] == "   " or self.board[self.location[0]+space][self.location[1]] == "TLS" or self.board[self.location[0]+space][self.location[1]] == "TWS" or self.board[self.location[0]+space][self.location[1]] == "DLS" or self.board[self.location[0]+space][self.location[1]] == "DWS" or self.board[self.location[0]+space][self.location[1]] == " * ":
                        current_board_ltr += " "
                    else:
                        current_board_ltr += self.board[self.location[0]+space][self.location[1]][1]
            else:
                return "Error: please enter a valid direction."

            if self.word not in dictionary:
                return "Please enter a valid dictionary word.\n"

            for letter in range(len(self.word)):
                if current_board_ltr[letter] == " ":
                    needed_tiles += self.word[letter]
                elif current_board_ltr[letter] != self.word[letter]:
                    print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                    return "The letters do not overlap correctly, please choose another word."

            #If there is a blank tile, remove it's given value from the tiles needed to play the word.
            if blank_tile_val != "":
                needed_tiles = needed_tiles[needed_tiles.index(blank_tile_val):] + needed_tiles[:needed_tiles.index(blank_tile_val)]

            #Ensures that the word will be connected to other words on the playing board.
            if (round_number != 1 or (round_number == 1 and players[0] != self.player)) and current_board_ltr == " " * len(self.word):
                print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                return "Please connect the word to a previously played letter."

            for letter in needed_tiles:
                if letter not in self.player.GetRack() or self.player.GetRack().count(letter) < needed_tiles.count(letter):
                    return "You do not have the tiles for this word\n"

            if self.location[0] > 14 or self.location[1] > 14 or self.location[0] < 0 or self.location[1] < 0 or (self.direction == "down" and (self.location[0]+len(self.word)-1) > 14) or (self.direction == "right" and (self.location[1]+len(self.word)-1) > 14):
                return "Location out of bounds.\n"

            if round_number == 1 and players[0] == self.player and self.location != [7,7]:
                return "The first turn must begin at location (7, 7).\n"
            return True

        else:
            if input("Are you sure you would like to skip your turn? (y/n)").upper() == "Y":
                if round_number == 1 and players[0] == self.player:
                    return "Please do not skip the first turn. Please enter a word."
                return True
            else:
                return "Please enter a word."

    def CalculateWordScore(self):
        global tile_dict, premium_spots
        word_score = 0
        for letter in self.word:
            for spot in premium_spots:
                if letter == spot[0]:
                    if spot[1] == "TLS":
                        word_score += tile_dict[letter] * 2
                    elif spot[1] == "DLS":
                        word_score += tile_dict[letter]
            word_score += tile_dict[letter]
        for spot in premium_spots:
            if spot[1] == "TWS":
                word_score *= 3
            elif spot[1] == "DWS":
                word_score *= 2
        self.player.IncreaseScore(word_score)

    def SetWord(self, word):
        self.word = word.upper()

    def SetLocation(self, location):
        self.location = location

    def SetDirection(self, direction):
        self.direction = direction

    def GetWord(self):
        return self.word


def turn(player, board, bag):
    #Begins a turn, by displaying the current board, getting the information to play a turn, and creates a recursive loop to allow the next person to play.
    global round_number, players, skipped_turns

    #If the number of skipped turns is less than 6 and a row, and there are either tiles in the bag, or no players have run out of tiles, play the turn.
    #Otherwise, end the game.
    if (skipped_turns < 6) or (player.rack.GetRackLength() == 0 and bag.GetRemainingTiles() == 0):

        #Displays whose turn it is, the current board, and the player's rack.
        print("\nRound " + str(round_number) + ": " + player.GetName() + "'s turn \n")
        print(board.GetBoardStr())
        print("\n" + player.GetName() + "'s Letter Rack: " + player.GetRack())

        #Gets information in order to play a word.
        word_to_play = input("Word to play: ")
        location = []
        col = input("Column number: ")
        row = input("Row number: ")
        if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
            location = [-1, -1]
        else:
            location = [int(row), int(col)]
        direction = input("Direction of word (right or down): ")

        word = Word(word_to_play, location, player, direction, board.GetBoardArr())

        #If the first word throws an error, creates a recursive loop until the information is given correctly.
        checked = word.CheckWord()
        while checked != True:
            print(checked)
            word_to_play = input("Word to play: ")
            word.SetWord(word_to_play)
            location = []
            col = input("Column number: ")
            row = input("Row number: ")
            if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                location = [-1, -1]
            else:
                word.SetLocation([int(row), int(col)])
                location = [int(row), int(col)]
            direction = input("Direction of word (right or down): ")
            word.SetDirection(direction)
            checked = word.CheckWord()

        #If the user has confirmed that they would like to skip their turn, skip it.
        #Otherwise, plays the correct word and prints the board.
        if word.GetWord() == "":
            print("Your turn has been skipped.")
            skipped_turns += 1
        else:
            board.PlaceWord(word_to_play, location, direction, player)
            word.CalculateWordScore()
            skipped_turns = 0

        #Prints the current player's score
        print("\n" + player.GetName() + "'s score is: " + str(player.GetScore()))

        #Gets the next player.
        if players.index(player) != (len(players)-1):
            player = players[players.index(player)+1]
        else:
            player = players[0]
            round_number += 1

        #Recursively calls the function in order to play the next turn.
        turn(player, board, bag)

    #If the number of skipped turns is over 6 or the bag has both run out of tiles and a player is out of tiles, end the game.
    else:
        end_game()

def start_game():
    #Begins the game and calls the turn function.
    global round_number, players, skipped_turns
    board = Board()
    bag = Bag()

    #Asks the player for the number of players.
    num_of_players = int(input("\nPlease enter the number of players (2-4): "))
    while num_of_players < 2 or num_of_players > 4:
        num_of_players = int(input("This number is invalid. Please enter the number of players (2-4): "))

    #Welcomes players to the game and allows players to choose their name.
    print("\nWelcome to Scrabble! Please enter the names of the players below.")
    players = []
    for i in range(num_of_players):
        players.append(Player(bag))
        players[i].SetName(input("Please enter player " + str(i+1) + "'s name: "))

    #Sets the default value of global variables.
    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game():
    #Forces the game to end when the bag runs out of tiles.
    global players
    highest_score = 0
    winning_player = ""
    for player in players:
        if player.get_score > highest_score:
            highest_score = player.IncreaseScore()
            winning_player = player.GetName()
    print("The game is over! " + winning_player + ", you have won!")

    if input("\nWould you like to play again? (y/n)").upper() == "Y":
        start_game()


if __name__ == "__main__":


    start_game()