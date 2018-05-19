import game
import numpy as np

import unittest



class GameTest(unittest.TestCase):
     def test_init(self):
         g = game.game()
         self.assertIsInstance(g, game.game_class.game)

     def test_get_grid(self):
     	g = game.game()
     	grid = g.get_grid()
     	self.assertIsInstance(grid, np.ndarray)
     	self.assertTrue(np.all(grid % 2 == 0))  # Control that we only have multiple of two