import unittest
from app.models.game import Game
from app.models.player import Player


class testGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("John", "Rock")
        self.player2 = Player("Mike", "Scissors")
        self.player3 = Player("Phil", "Paper")

    def test_rock_beats_scissors(self):
        result = Game.get_the_winner(self.player1, self.player2)
        self.assertEqual(self.player1, result)

    def test_scissors_beats_paper(self):
        result = Game.get_the_winner(self.player2, self.player3)
        self.assertEqual(self.player2, result)

    def test_paper_beats_rock(self):
        result = Game.get_the_winner(self.player3, self.player1)
        self.assertEqual(self.player3, result)

    def test_for_a_draw(self):
        result = Game.get_the_winner(self.player3, self.player3)
        self.assertEqual(None, result)
