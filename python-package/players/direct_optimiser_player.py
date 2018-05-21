import game
import random
import copy
import numpy as np

class direct_optimiser_player():
	"""Direct moove optimiser choose the moove which give it the biggest digit at next step."""
	def __init__(self, n_forward = 1):
		if n_forward != 1:
			raise ValueError("direct_optimiser_player: n_forward != 1 is not implemented yet")
		self.n_forward = n_forward

	def strategie(self, g):
		largest = g.largest()
		best_dir = None
		for direction in game.directions:
			_g = copy.deepcopy(g)
			_g.moove(direction)
			if np.any(_g.get_grid() != g.get_grid()): # Moove should at least change the map
				if _g.largest() >= largest:
					largest = _g.largest()
					best_dir = direction

		if best_dir is None: # If didn't find any intersting moove: random
			best_dir = random.sample(game.directions, 1)[0]
		return(best_dir)

__all__ = ["direct_optimiser_player"]