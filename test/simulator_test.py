from simulator import *
from players import random_player
import unittest
import game



class EvaluatorTest(unittest.TestCase):
	def evaluator_test(self):
		self.assertIsInstance(evaluator(random_player), dict)


class BenchmarkTest(unittest.TestCase):
	def benchmark_test(self):
		self.assertIsNone(benchmark())

