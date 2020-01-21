import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid),9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_empty_word_is_invalid(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ')                   # force grid
        self.assertIs(new_game.is_valid('EUREKA'), True)    # test a valid answer
        self.assertEqual(new_game.grid, list('KWEUEAKRZ'))  # test grid is not changed

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ')                   # force grid
        self.assertIs(new_game.is_valid('NOTWORKING'),False)# should return an error
        self.assertEqual(new_game.grid, list('KWEUEAKRZ'))  # test grid is not changed

    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW')
        self.assertIs(new_game.is_valid('FEUN'), False)

