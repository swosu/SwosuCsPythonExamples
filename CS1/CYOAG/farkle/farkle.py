import random

class Player(object):
    """A player in the game of Farkel."""

    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __ne__(self, other):
        return self.name != other.name
    
    def __lt__(self, other):
        return self.score < other.score
    

class Farkel(object):
    """A game of Farkel."""

    def __init__(self, players):
        self.players = players
        self.current_player = 0
        self.turn_score = 0
        self.dice = [0, 0, 0, 0, 0]

    def play(self):
        """Play the game."""

        """ who goes first? """
        self.current_player = random.randint(0, len(self.players) - 1)
        print(self.players[self.current_player].name, 'goes first')


        while not self.game_over():
            self.take_turn()
        self.print_scores()

    def game_over(self):
        """Return True if the game is over."""
        for player in self.players:
            if player.score >= 10000:
                return True
        return False
    
    def print_scores(self):
        """Print the scores of all players."""
        self.players.sort(reverse=True)
        for player in self.players:
            print(player.name, 'scored', player.score)

    def take_turn(self):
        """Play a turn for the current player."""
        self.roll_dice()
        self.print_dice()
        while self.turn_score < 300 and self.has_scoring_dice():
            self.take_action()
            self.print_dice()
        self.players[self.current_player].score += self.turn_score
        print(self.players[self.current_player].name, 'scored', self.turn_score)
        self.turn_score = 0
        self.current_player = (self.current_player + 1) % len(self.players)

    def roll_dice(self):
        """Roll all of the dice."""
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(1, 6)

    def print_dice(self):
        """Print the current dice."""
        print(' '.join([str(d) for d in self.dice]))

    def has_scoring_dice(self):
        """Return True if there are scoring dice."""
        for die in self.dice:
            if die == 1 or die == 5:
                return True
        return False

    def take_action(self):
        """Take an action for the current player."""
        action = input('Roll or bank? ')
        if action == 'r' or action == 'roll':
            self.roll_again()
        elif action == 'b' or action == 'bank':
            self.bank_points()
        else:
            print('Invalid action')

    def roll_again(self):
        """Roll the dice that the player wants to roll again."""
        roll_again = input('Which dice to roll again (1-5, 0 to stop)? ')
        while roll_again != '0':
            self.dice[int(roll_again) - 1] = random.randint(1, 6)
            roll_again = input('Which dice to roll again (1-5, 0 to stop)? ')

    def bank_points(self):
        """Bank the points for the current turn."""
        self.turn_score += self.get_turn_score()

    def get_turn_score(self):
        """Return the score for the current turn."""
        score = 0
        dice = self.dice[:]
        dice.sort()
        score += self.get_score_for_number(dice, 1, 100)
        score += self.get_score_for_number(dice, 5, 50)
        score += self.get_score_for_run(dice, 3, 1000)
        score += self.get_score_for_run(dice, 4, 2000)
        score += self.get_score_for_run(dice, 5, 4000)
        return score
    
    def get_score_for_number(self, dice, number, points):
        """Return the score for a number."""
        count = dice.count(number)
        return count * points
    
    def get_score_for_run(self, dice, length, points):
        """Return the score for a run."""
        score = 0
        while self.has_run(dice, length):
            score += points
            for i in range(length):
                dice.remove(dice[0])
        return score
    
    def has_run(self, dice, length):
        """Return True if there is a run of the specified length."""
        if len(dice) < length:
            return False
        for i in range(length - 1):
            if dice[i] != dice[i + 1] - 1:
                return False
        return True
    
    



if __name__ == '__main__':
    # get number of users for farkel game
    num_players = int(input('How many players? '))

    # create a list of players
    players = []
    for i in range(num_players):
        name = input('Enter player name: ')
        player = Player(name)
        players.append(player)

    # play the game
    game = Farkel(players)
    game.play()
