# -*- coding: utf-8 -*-
import game
import random

class single_moove_player():
	"""Single moove player choose a moove at init and perform always the same moove"""
	def __init__(self):
		self.direction =  random.sample(game.directions, 1)[0]
		
	def strategie(self, g):
		return(self.direction)

__all__ = ["single_moove_player"]