import GameAgent as g
from random import randrange, choice
#initialize the game
game = g.GameField(height=2, width=2, win=32)

class RamdomPolicy(object):
	def __init__(self):
		self.pool = ['Up', 'Left', 'Down', 'Right']

	def reset(self):
		del self.pool
		self.pool = ['Up', 'Left', 'Down', 'Right']
	
	def generate(self, action=None):
		if action:
			self.pool.remove(action)
		return choice(self.pool)

rpolicy = RamdomPolicy()
records =[]

#repeat the game 1000 times
for i in range(10000):
	#reset the game
	game.reset()
	while (not game.is_win()) and (not game.is_gameover()):
		rpolicy.reset()
		action = rpolicy.generate()
		while not game.move(action):
			action = rpolicy.generate(action)

	print "time ",i,":",game.score
	records.append((game.is_win(),game.score))