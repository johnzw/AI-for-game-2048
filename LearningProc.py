import GameAgent as g
from random import randrange, choice, random
import numpy as np
import math
import pickle
import argparse

#initialize the array
array = np.zeros((7000,4))

# #array from the file
# with open("array.data","r") as f:
# 	array = pickle.load(f)
# #model
# model = {}

actionTranslate = ['Up', 'Left', 'Down', 'Right']

class QLearning(object):
	def __init__(self, greedy=None):
		self.pool = [0,1,2,3]
		if greedy == None:
			#default
			greedy = 0.97
		self.greedy = greedy

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




def train(mode=False,alpha = None,countingTimes = None, greedy=None):
	#set the configuration
	if alpha==None:
		alpha = 0.7
	if countingTimes == None:
		countingTimes = 500000

	global array
	#initialize the game
	game = g.GameField(height=2, width=2, win=32)
	#initalize the Learning engine
	q = QLearning(greedy)
	#set the list to store all the results
	records =[]
	for i in range(countingTimes):
		#reset the game
		game.reset()
		while (not game.is_win()) and (not game.is_gameover()):
			
			state = q.fieldToState(game.field)
			q.reset()
			action = q.generateAction(state)

			while not game.move(actionTranslate[action]):
				action = q.generateAction(state, action)

			#the mode
			if mode == False:
				if game.is_win():
					reward = game.score
				else:
					reward = 0
			else:
				reward = game.reward

			array[state][action] += alpha * (reward+array[q.fieldToState(game.field)].max()-array[state][action])
			#save into the model
			# model[(state,action)] = (reward, q.fieldToState(game.field))
			# for repeat in range(50):
			# 	s,a = choice(model.keys())
			# 	r,s1 = model[(s,a)]
			# 	array[s][a] += alpha * (r+array[s1].max()-array[s][a])
		print "time ",i,"game score:",game.score
		records.append((game.is_win(),game.score))

	return records

def recordStat(records):
	win = [i[0] for i in records]
	win_distribute = [win[sli:(sli+1000)].count(True) for sli in range(0,len(win),1000)]

if __name__ == '__main__':
	#set the argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-a","--alpha", help="learning step alpha for QLearning, defualt:0.7",type=float)
	parser.add_argument("-t","--times", help="learning times for QLearning, defualt:500000",type=int)
	parser.add_argument("--reward", help="enable the reward to be score of every move, otherwise reward only being the finel score of the game",action="store_true")
	parser.add_argument("-g","--greedy", help="greedy level of QLearning, defualt:0.97",type=float)
	args = parser.parse_args()

	#it still has bug, user might input unexpected paras
	records = train(mode=args.reward, alpha=args.alpha, countingTimes=args.times, greedy=args.greedy)
	win_distribute = recordStat(records)

	#dump the array.data file
	with open("array.data","w") as f:
	 	pickle.dump(array, f)
	