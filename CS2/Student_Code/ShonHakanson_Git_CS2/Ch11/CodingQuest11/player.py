from dice import dice

class Player:
    """Represents a player in the dice game."""

    def __init__(self, name):
        self.name = name
        self.score = 0
        # Each player gets two dice
        self.dice = [dice(), dice()]

    def roll_dice(self):
        """Roll both dice and return a list of their values."""
        rolls = [die.roll() for die in self.dice]
        print(f"{self.name} rolled {rolls}")
        return rolls

    def add_score(self, points):
        """Add points to the player's score."""
        self.score += points

    def reset_score(self):
        """Reset the player's score to 0."""
        self.score = 0

    def __str__(self):
        """String representation for clean printing."""
        return f"{self.name} (Score: {self.score})"
