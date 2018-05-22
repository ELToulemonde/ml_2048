# -*- coding: utf-8 -*-
import game
import random
import sys

class random_player():
	def __init__(self, seed = random.randrange(sys.maxsize)):
		self.seed = seed
		random.seed(seed)

	def strategie(self, g):
		"""Random player choose randomnly a moove"""
		direction = random.sample(game.directions, 1)[0]
		return(direction)


__all__ = ["random_player"]