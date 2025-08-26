#write unit tests for a yahtzee game for python

import unittest
from YahtzeeGame import YahtzeeGame

class TestYahtzeeGame(unittest.TestCase):
    def setUp(self):
        self.game = YahtzeeGame()
 
    def test_roll_dice(self):
        self.game.roll_dice()
        self.assertEqual(len(self.game.dice), 5)
 
    def test_score_ones(self):
        self.game.dice = [1, 2, 3, 4, 5]
        score = self.game.score_ones()
        self.assertEqual(score, 1)
 
    def test_score_twos(self):
        self.game.dice = [1, 2, 2, 4, 5]
        score = self.game.score_twos()
        self.assertEqual(score, 4)
 
    def test_score_threes(self):
        self.game.dice = [3, 3, 3, 4, 5]
        score = self.game.score_threes()
        self.assertEqual(score, 9)
 
    def test_score_fours(self):
        self.game.dice = [4, 4, 3, 4, 5]
        score = self.game.score_fours()
        self.assertEqual(score, 12)
 
    def test_score_fives(self):
        self.game.dice = [4, 5, 5, 4, 5]
        score = self.game.score_fives()
        self.assertEqual(score, 15)
 
    def test_score_sixes(self):
        self.game.dice = [4, 6, 6, 4, 5]
        score = self.game.score_sixes()
        self.assertEqual(score, 12)
 
    def test_three_of_a_kind(self):
        self.game.dice = [4, 6, 6, 6, 5]
        score = self.game.three_of_a_kind()
        self.assertEqual(score, 18)
 
    def test_four_of_a_kind(self):
        self.game.dice = [6, 6, 6, 6, 5]
        score = self.game.four_of_a_kind()
        self.assertEqual(score, 24)
 
    def test_full_house(self):
        self.game.dice = [6, 6, 3, 3, 6]
        score = self.game.full_house()
        self.assertEqual(score, 25)
 
    def test_small_straight(self):
        self.game.dice = [4, 2, 3, 5, 1]
        score = self.game.small_straight()
        self.assertEqual(score, 30)
 
    def test_large_straight(self):
        self.game.dice = [4, 5, 2, 6, 3]
        score = self.game.large_straight()
        self.assertEqual(score, 40)
 
    def test_yahtzee(self):
        self.game.dice = [4, 4, 4, 4, 4]
        score = self.game.yahtzee()
        self.assertEqual(score, 50)
 
    def test_chance(self):
        self.game.dice = [4, 4, 4, 1, 2]
        score = self.game.chance()
        self.assertEqual(score, 15)
 
if __name__ == '__main__':
    unittest.main()