
from random import randrange, choice, random
import numpy as np
import math
import pickle

with open("array.data","r") as f:
	array = pickle.load(f)

actionTranslate = ['Up', 'Left', 'Down', 'Right']
class QLearning(object):
	def __init__(self):
		self.pool = [0,1,2,3]
		self.greedy = 1

	def reset(self):
		del self.pool
		self.pool = [0,1,2,3]
	
	def generateAction(self, state, action=None):
		if action:
			self.pool.remove(action)

		if random()<self.greedy:
			#go greedy way
			a = array[state].argmax()
			if a in self.pool:
				return a
			else:
				return choice(self.pool)
		else:
			return choice(self.pool)

	def fieldToState(self, field):
		output = 0
		for i in range(2):
			for j in range(2):
				num = 0
				if field[i][j]:
					num = int(math.log(field[i][j],2))
				output += num*(10**(2*i+j))
		return output

	def makeMove(self, field):
		state = self.fieldToState(field)
		action_num = self.generateAction(state)
		return actionTranslate[action_num]