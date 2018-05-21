# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:53:40 2018

@author: TOULEEM
"""
import numpy as np
import random
from .piles_class import pile, piles


directions = ["up", "right", "left", "down"]

def _is_direction(direction):
    if not direction in directions:
        raise ValueError("direction should be in " + str(directions))

class game:
    # Init function
    # --------------
    def __init__(self, grid_size = 4, proba_of_4 = 0.25):
        self.grid_size = grid_size
        self.proba_of_4 = proba_of_4
        self.__grid = np.zeros((grid_size, grid_size))
        self.__add_digit()
        self.__directions = {"down": (0, range(self.__grid.shape[0] - 1, -1, -1)),
                             "up": (0, range(self.__grid.shape[0])),
                             "left": (1, range(self.__grid.shape[1] - 1, -1, -1)),
                             "right": (1, range(self.__grid.shape[1]))
                             }
    # Getter
    # ------
    def get_grid(self):
        return(self.__user_grid())

    # Moove
    # -----
    def moove(self, direction):
        """
        Perform a moove on grid
        """
        # Sanity check
        _is_direction(direction)
        # Perform moove
        _piles = self.__build_piles(direction)
        _piles.moove()
        _store_grid = np.copy(self.__grid)
        self.__apply_piles(_piles, direction)
        # To-do comparing grid might not be the fastest, could we control the _piles?
        if np.any(_store_grid != self.__grid): # If moove changed something change add random digit
            # Add a random digit
            self.__add_digit()
        # else do nothing

    def __apply_piles(self, _piles, direction):
        """Replace grid by piles
        :param _piles: Piles to apply
        :param direction: Direction to apply it
        :type _piles: piles
        :type direction: str
        """
        # Sanity check
        _is_direction(direction)

        if self.__directions[direction][0] == 0:
            for j in range(0, self.__grid.shape[1]):
                _pile = _piles.piles[j]
                self.__grid[self.__directions[direction][1], j] = _pile.pile
        else:
            for i in range(0, self.__grid.shape[0]):
                _pile = _piles.piles[i]
                self.__grid[i, self.__directions[direction][1]] = _pile.pile

    def __build_piles(self, direction):
        """Build a list of list considered as piles
        :param direction: Direction to apply it
        :type direction: str
        """
        # Sanity check
        _is_direction(direction)
        # Initialize piles
        _piles = piles()
        # Compute piles
        if self.__directions[direction][0] == 0:
            for j in range(0, self.__grid.shape[1]):
                _pile = pile(self.__grid[self.__directions[direction][1], j])
                _piles.append(_pile)
        else:
            for i in range(0, self.__grid.shape[0]):
                _pile = pile(self.__grid[i, self.__directions[direction][1]])
                _piles.append(_pile)
        # Return
        return(_piles)

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
        
    def largest(self):
        return(2 ** np.max(self.__grid, axis = (0,1)))

    def win(self, objectif = 2048):
        """Player won if he reached objectif"""
        if not isinstance(objectif, int):
            raise ValueError("game.win: objectif should be an integer")

        return(self.largest() == objectif)

    def lost(self):
        """Player as lost if no moove change something"""
        lost = True
        for direction in directions:
            _piles = self.__build_piles(direction)
            _piles.moove()
            if self.__build_piles(direction) != _piles:
                lost = False
        return(lost)



## All list
#-----------
__all__ = ["game", "directions"]