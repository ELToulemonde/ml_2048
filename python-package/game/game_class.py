# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:53:40 2018

@author: TOULEEM
"""
import numpy as np
import random
class game:
    # Init function
    # --------------
    def __init__(self, grid_size = 4, proba_of_4 = 0.25):
        self.grid_size = grid_size
        self.proba_of_4 = proba_of_4
        self.__grid = np.zeros((grid_size, grid_size))
        self.__add_digit()

    # Getter
    # ------
    def get_grid(self):
        return(self.__user_grid())

    ## User grid
    # -----------
    # In order to reduce storage, we keep only power of 2 digits. But to print it, we have to 
    # print to user we have to give it it's right shape
    def __user_grid(self):
        grid = 2 ** self.__grid
        grid[grid == 1] = 0
        return(grid)

    def __add_digit(self):
        selected_cell = random.sample(self.__empty_cells(), 1)[0]
        self.__grid[selected_cell] = 1 + int(random.random() < self.proba_of_4)
        
    def __empty_cells(self):
        empty_list = []
        for i in range(self.__grid.shape[0]):
            for j in range(self.__grid.shape[1]):
                if self.__grid[i, j] == 0:
                    empty_list.append((i,j))
        return(empty_list)
        
    def print(self):
        print(self.__user_grid())
        

        
if __name__ == "__main__":
    g = game()
    g.print()
    