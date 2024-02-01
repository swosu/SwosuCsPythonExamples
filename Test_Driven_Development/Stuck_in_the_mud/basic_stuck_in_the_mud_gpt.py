import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.roll = []

    def roll_dice(self):
        roll = random.randint(1, 6)
        print(f"{self.name} rolled a {roll}")
        return roll

    def add_points(self, points):
        self.score += points

class StuckInTheMudGame:
    def __init__(self, players, inning_score=100):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.winning_score = winning_score
        self.current_player = self.player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play(self):
        while True:
            print(f"{self.current_player.name}'s turn:")
            input("Press Enter to roll the dice...")

            roll = self.current_player.roll_dice()

            if roll == 1:
                print("Oops, you rolled a 1! You lose your turn and all your points.")
                self.current_player.score = 0
            else:
                self.current_player.add_points(roll)
                print(f"Current score: {self.current_player.score}")

                if self.current_player.score >= self.winning_score:
                    print(f"{self.current_player.name} wins!")
                    break

            self.switch_player()

if __name__ == "__main__":
    # make an array of player objects based on the Player class
    players = []
    while True:
        player_name = input("Enter a player's name (or enter -1 to start the game): ")
        if player_name == "-1":
            if len(players) < 2:
                print("You need at least two players to start the game.")
                continue
            else:
                break
        players.append(player_name)

    if len(players) >= 2:
        game = StuckInTheMudGame(players)
        game.play()
    else:
        print("Not enough players to start the game.")
