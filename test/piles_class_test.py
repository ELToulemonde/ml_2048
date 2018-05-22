# -*- coding: utf-8 -*-
import numpy as np
from game.piles_class import *
import unittest



class PilesTest(unittest.TestCase):
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

	def test_append_pile(self):
		pile1 = pile()
		pile1.append(1)
		pile2 = pile([1])
		self.assertTrue(pile1 == pile2)

	def test_append_piles(self):
		# Should only accept up, down, right, left
		piles1 = piles()
		self.assertRaises(ValueError, piles1.append, 1)

	def test_eq_pile(self):
		# Test equality
		pile1 = pile([1, 1, 0, 0])
		pile2 = pile([1, 1, 0, 0])
		self.assertTrue(pile1 == pile2)
		# Test unequality
		pile3 = pile([2, 1, 0, 0])
		self.assertFalse(pile1 == pile3)

	def test_eq_piles(self):
		# test equality
		pile1 = pile([1, 1, 0, 0])
		piles1 = piles()
		piles1.append(pile1)
		piles2 = piles()
		piles2.append(pile1)
		self.assertTrue(piles1 == piles2)
		# Test un-equality
		piles3 = piles()
		self.assertFalse(piles1 == piles3)

if __name__ == '__main__':
    unittest.main()