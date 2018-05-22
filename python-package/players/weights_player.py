# -*- coding: utf-8 -*-
import game
import random
import numpy as np

class weights_player():
	def __init__(self, weights):
		self.weights =  weights
		self.__cost_function = lambda x: np.sum(np.multiply(x, self.weights), axis = (0, 1))

	def strategie(self, g):
		# Sanity check
		if g.get_grid().shape != self.weights.shape:
			raise ValueError("weights_player: weights should have the same dimensions as game.grid_size")
		# Initialize best perf
		best_perf = self.__cost_function(g.get_grid())
		best_dir = None
		# Look for best moove
		for direction in game.directions:
			_g = copy.deepcopy(g)
			_g.moove(direction)
			if np.any(_g.get_grid() != g.get_grid()): # Moove should at least change the map
				if self.__cost_function(_g.get_grid()) >= best_perf:
					best_perf = self.__cost_function(_g.get_grid())
					best_dir = direction
		if best_dir is None: # If didn't find any intersting moove: random
			best_dir = random.sample(game.directions, 1)[0]
		return(best_dir)

import numpy as np
import random
class genetic_learn_weights():
    def __init__(self, n_indivudals = 100, grid_size = 4):
        self.n_indivudals = n_indivudals
        self.grid_size = grid_size
        self.weights_ = [np.random.random(size = (self.grid_size, self.grid_size)) for _ in range(self.n_indivudals)]
        
    def fit(self, n_epoch = 10, kill_rate = 0.1, mutation_rate = 0.05):
        # Random initialization of list of individuals
        for epoch in range(n_epoch):
            print("Epoch: " + str(epoch))
            # Evaluate
            perfs_ = []
            for weight in self.weights_:
                p = weights_player(weight)
                perfs_.append(evaluator(p.strategie)["perf"])
            self.perfs_ = perfs_    
            print("Perfs: " + str(np.mean(perfs_)))
            # Kill
            min_perf_to_survice = np.percentile(perfs_, kill_rate * 100)
            self.weights_ = [weight for weight, perf in zip(self.weights_, perfs_) if perf > min_perf_to_survice]
            
            # Reproduce
            n_child = self.n_indivudals - len(self.weights_)
            parents = np.random.choice(range(len(self.weights_)),  n_child * 2, replace = True)
            for i in range(n_child):
                parent1_id = parents[i]
                parent2_id = parents[i + n_child]
                child = (self.weights_[parent1_id] + self.weights_[parent2_id]) / 2
                self.weights_.append(child)
                
            # Mutate:
            """
            for i in range(self.n_indivudals):
                # Each cell of the grid has z probability of having a change of mutation_rate
                mutations_zone = np.random.random(size =(self.grid_size, self.grid_size)) > 1 - mutation_rate
                n_mutations = np.sum(mutations_zone)
                # The mutation consists of a random incremet of the cell
                self.weights_[i][mutations_zone] = self.weights_[i][mutations_zone] + np.random.normal(size = n_mutations)
                """
            self.weights_ = [weight + mutation_rate * np.random.normal(size = weight.shape) for weight in self.weights_]
                
 
if __name__ == "__main__":           
    glw = genetic_learn_weights(n_indivudals = 100)
    glw.fit(n_epoch = 10, kill_rate = 0.33, mutation_rate = 0.2)
    print("2")
    glw.fit(n_epoch = 10, kill_rate = 0.33, mutation_rate = 0.1)
    print("3")
    glw.fit(n_epoch = 10, kill_rate = 0.33, mutation_rate = 0.05)
    print("4")
    glw.fit(n_epoch = 10, kill_rate = 0.2, mutation_rate = 0.05)
    print("5")
    glw.fit(n_epoch = 10, kill_rate = 0.1, mutation_rate = 0.05)
    print("6")
    glw.fit(n_epoch = 10, kill_rate = 0.1, mutation_rate = 0.025)
    print("7")
    glw.fit(n_epoch = 10, kill_rate = 0.05, mutation_rate = 0.025)
    print("8")
    glw.fit(n_epoch = 100, kill_rate = 0.2, mutation_rate = 0.025)
    
__all__ = ["weights_player"]