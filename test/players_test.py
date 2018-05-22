# -*- coding: utf-8 -*-
from players import *
import unittest
import game
import random
import numpy as np

class PlayersTest(unittest.TestCase):
	def test_random_player(self):
		g = game.game()
		self.assertTrue(random_player().strategie(g) in game.directions)

	def test_single_moove_player(self):
		g = game.game()
		self.assertTrue(single_moove_player().strategie(g) in game.directions)

	def test_direct_optimiser_player(self):
		g = game.game()
		g._game__grid = np.array([[2, 2, 0, 0],  [2, 0, 0, 0], [4, 0, 0, 4], [0, 0, 0, 0]])
		self.assertTrue(direct_optimiser_player().strategie(g) == "left")

	def test_weights_player(self):
		g = game.game()
		self.assertIsInstance(weights_player().strategie(g), str)

if __name__ == '__main__':
    unittest.main()