import GameAgent as g
from random import randrange, choice, random
import numpy as np
import math
import pickle
#initialize the game
game = g.GameField(height=2, width=2, win=32)


# array = np.zeros((7000,4))
with open("array.data","r") as f:
	array = pickle.load(f)
#model
model = {}
actionTranslate = ['Up', 'Left', 'Down', 'Right']
class QLearning(object):
	def __init__(self):
		self.pool = [0,1,2,3]
		self.greedy = 0.97

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


q = QLearning()
records =[]
alpha = 0.7



#repeat the game 1000 times
for i in range(500000):
	#reset the game
	game.reset()
	while (not game.is_win()) and (not game.is_gameover()):
		state = q.fieldToState(game.field)
		q.reset()
		action = q.generateAction(state)
		while not game.move(actionTranslate[action]):
			action = q.generateAction(state, action)

		if game.is_win():
			reward = game.score
		else:
			reward = 0

		array[state][action] += alpha * (reward+array[q.fieldToState(game.field)].max()-array[state][action])
		#save into the model
		# model[(state,action)] = (reward, q.fieldToState(game.field))
		# for repeat in range(50):
		# 	s,a = choice(model.keys())
		# 	r,s1 = model[(s,a)]
		# 	array[s][a] += alpha * (r+array[s1].max()-array[s][a])

	print "time ",i,":",game.score
	records.append((game.is_win(),game.score))

win = [i[0] for i in records]
win_distribute = [win[sli:(sli+1000)].count(True) for sli in range(0,500000,1000)]