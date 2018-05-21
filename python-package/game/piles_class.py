import numpy as np
class pile():
	"""A pile is a list of element with a moove function"""
	def __init__(self, value = []):
		self.pile = value

	def append(self, value):
		"""pile.append allows you to add an element to a pile
		"""
		self.pile.append(value)

	def moove(self):
		"""
		pile.moove is to tranform a pile
		Ex1: pile is [1,1,0,0] it will become [2,0,0,0]
		Ex2: pile is [2,1,1,0] it will become [2,2,0,0]
		Ex3: pile is [3,2,1,0] it will stay [3,2,1,0]
		Ex4: pile is [2,2,2,2] it will become [3,3,0,0]
		Ex5: pile is [0,0,2,2] it will become [3,0,0,0]
		Ex6: pile is [0,2,0,2] it will become [3,0,0,0]
		"""
		new_pile = []
		old_pile = [elt for elt in self.pile if elt != 0] # drop 0s
		i = 0
		while i <= len(old_pile) - 1: # -1 because we are looking at i and i + 1
			if i <= len(old_pile) - 2 and old_pile[i] == old_pile[i + 1]:
				new_pile.append(old_pile[i] + 1)
				i += 2 # Treated both elements
			else:
				new_pile.append(old_pile[i])
				i += 1 #Treated only one element

		# We add 0s so that new_pile and pile have the same len
		while len(new_pile) < len(self.pile):
			new_pile.append(0)

		# We replace pile by new_pile
		self.pile = new_pile
	
	# Equality function
	## ----------------
	def __eq__(self, other):
		"""Overrides the default implementation"""
		if isinstance(self, other.__class__):
			return np.all(self.pile == other.pile)
		return False

class piles():
	"""Piles is a list of pile"""
	def __init__(self):
		self.piles = []

	def append(self, value):
		"""Append a pile on piles"""
		if isinstance(value, pile):
			self.piles.append(value)
		else:
			raise ValueError("piles.append: value should be of type pile")

	def moove(self):
		"""Perform moove on each pile of the piles."""
		for i in range(len(self.piles)):
			self.piles[i].moove()
	
	# Equality function
	## ----------------
	def __eq__(self, other):
		"""Overrides the default implementation"""
		if isinstance(self, other.__class__):
			return self.__dict__ == other.__dict__
		return False



__all__ = ["pile", "piles"]