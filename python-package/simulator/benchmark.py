from players import *
from .evaluator import *

def benchmark(n_itr = 20):
	player_list = [random_player, single_moove_player, direct_optimiser_player]

	for player in player_list:
		perf = 0
		time = 0
		player_init = player()
		strategie = player_init.strategie
		for _ in range(n_itr):
			eval = evaluator(strategie, n_max_moove = 500)
			perf += eval["perf"] / n_itr
			time += eval["duration"] / n_itr

		print(str(player) + " perf: " + str(perf))
		print(str(player) + " time: " + str(time))