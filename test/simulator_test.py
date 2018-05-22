# -*- coding: utf-8 -*-
from simulator import *
from players import random_player
import unittest
import game



class SimulatorTest(unittest.TestCase):
	def test_evaluator(self):
		self.assertIsInstance(evaluator(random_player), dict)

	def test_benchmark(self):
		self.assertIsNone(benchmark())


if __name__ == '__main__':
    unittest.main()