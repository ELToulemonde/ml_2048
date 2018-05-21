import game
import numpy as np
import random
import unittest
from game.piles_class import *


class GameTest(unittest.TestCase):
	# Test initiatialisation of the game
	def test_init(self):
		g = game.game()
		self.assertIsInstance(g, game.game_class.game)
	# Test grid getter
	def test_get_grid(self):
		g = game.game()
		grid = g.get_grid()
		self.assertIsInstance(grid, np.ndarray)
		self.assertTrue(np.all(grid % 2 == 0))  # Control that we only have multiple of two

	def test__build_piles(self):
		# Perform computation
		random.seed(42) # Fix seed
		g = game.game()
		grid = g.get_grid()
		_piles = g._game__build_piles("up")

		# Build expected result to compare
		expected_piles = piles()
		expected_piles.append(pile([0., 0., 0., 0.]))
		expected_piles.append(pile([0., 0., 0., 0.]))
		expected_piles.append(pile([0., 0., 0., 0.]))
		expected_piles.append(pile([2., 0., 0., 0.]))

		# Control
		self.assertTrue(_piles == expected_piles)

	def test__apply_piles(self):
		# Perform computation
		random.seed(42) # Fix seed
		direction = "down" # Choose one direction
		g = game.game()
		_piles = g._game__build_piles(direction)
		_piles.moove()
		g._game__apply_piles(_piles, direction)
		grid = g.get_grid()
		# Build expected result to compare
		expected_grid = np.array([[0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 4.]])
		# Control
		self.assertTrue(np.all(grid == expected_grid))

	# Test moove
	def test_moove(self):
		random.seed(42) # Fix seed
		g = game.game()

		# Control that mooves have correct actions
		# Up moove
		g.moove("up") # Moove do nothing
		self.assertTrue(np.all(g.get_grid() == np.array([[0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])))
		# Down moove
		g.moove("down")
		self.assertTrue(np.all(g.get_grid() == np.array([[0, 0, 0, 0], [4., 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4.]])))
		# Left moove
		g.moove("left")
		self.assertTrue(np.all(g.get_grid() == np.array([[0, 0, 2, 0],  [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 4]])))
		# Right moove
		g.moove("right")
		self.assertTrue(np.all(g.get_grid() == np.array([[2, 0, 0, 0],  [4, 0, 0, 0], [0, 0, 0, 0], [4, 2, 0, 0]])))

		# Up moove
		g.moove("up")
		self.assertTrue(np.all(g.get_grid() == np.array([[2, 2, 0, 0],  [8, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0]])))
		# Should only accept up, down, right, left
		self.assertRaises(ValueError, g.moove, "cdy")

	def test_largest(self):
		random.seed(42) # Fix seed
		g = game.game()
		self.assertTrue(g.largest() == 4)

	def test_win(self):
		g = game.game()
		g._game__grid = np.array([[11, 0, 3, 4],  [4, 3, 2, 1], [4, 3, 2, 1], [1, 2, 3, 4]])
		self.assertTrue(g.win())

	def test_lost(self):
		g = game.game()
		# Change grid to make it lost
		g._game__grid = np.array([[1, 2, 3, 4],  [4, 3, 2, 1], [1, 2, 3, 4], [4, 3, 2, 1]])
		print(g._game__grid)
		self.assertTrue(g.lost())