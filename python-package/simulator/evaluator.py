# -*- coding: utf-8 -*-
import game
import time
def evaluator(strategie, n_max_moove = 2000):
	"""Evaluator allows you to simulate a game and get some feed back
	
	:param strategie: Player strategie given a game.game return a direction
    :param n_max_moove: Max number of moove to simulate
    :type strategie: function
    :type n_max_moove: int
    :return: The result of simulation: {failed: Bool Failed or not, 
    									win: Bool Win, 
    									perf: biggest number a the end,
    									n_mooves: int number of mooves before breaking, 
    									"largests": largest at each moove,
    									"duration": TIme to simulate}
    :rtype: dict

	"""

	# To-do control that the strategy, take a game and return a moove

	## Initialize
	# Game
	g = game.game()
	# Storing variables
	n_mooves = 0
	failed = False # Is the strategy correct
	start_time = time.time()

	## Computation
	while not g.lost() and not g.win() and n_mooves < n_max_moove:
		# Retrieve direction
		direction = strategie(g)
		# Control direction
		if direction not in game.directions:
			failed = True
			break
		# Perform moove
		g.moove(direction)
		# Store values

		n_mooves += 1

	## Return
	return({"failed": failed, 
		    "win": g.win(), 
		    "lost": g.lost(),
		    "perf": g.largest(), 
		    "n_mooves": n_mooves,
		    "duration": time.time() - start_time})


__all__ = ["evaluator"]