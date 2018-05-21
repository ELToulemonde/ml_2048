import numpy as np
from game.piles_class import *
import unittest



class PilesTest(unittest.TestCase):
	# Test internal function _sort_piles
	def test_moove(self):
		my_piles = piles()
		my_piles.append(pile([1, 1, 0, 0]))
		my_piles.append(pile([2, 1, 1, 0]))
		my_piles.append(pile([3, 2, 1, 0]))
		my_piles.append(pile([2, 2, 2, 2]))
		my_piles.append(pile([0, 0, 2, 2]))
		my_piles.append(pile([0, 2, 0, 2]))
		my_piles.moove()
		self.assertTrue(np.all(my_piles.piles[0] == pile([2, 0, 0, 0])))
		self.assertTrue(np.all(my_piles.piles[1] == pile([2, 2, 0, 0])))
		self.assertTrue(np.all(my_piles.piles[2] == pile([3, 2, 1, 0])))
		self.assertTrue(np.all(my_piles.piles[3] == pile([3, 3, 0, 0])))
		self.assertTrue(np.all(my_piles.piles[4] == pile([3, 0, 0, 0])))
		self.assertTrue(np.all(my_piles.piles[5] == pile([3, 0, 0, 0])))

	def test_eq_pile(self):
		pile1 = pile([1, 1, 0, 0])
		pile2 = pile([1, 1, 0, 0])
		self.assertTrue(pile1 == pile2)

	def test_eq_piles(self):
		pile1 = pile([1, 1, 0, 0])
		piles1 = piles()
		piles1.append(pile1)
		piles2 = piles()
		piles2.append(pile1)
		self.assertTrue(piles1 == piles2)
