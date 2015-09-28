import GameAgent2
import GameAgent
import json
from random import choice
actionTranslate = ['Up', 'Left', 'Down', 'Right']

agent = GameAgent2.GameField()
discount = 0.95		
def explore(field, level):
	if level == 1:
		record = []
		#for all the posible move 
		for move in actionTranslate:
			#set the field
			agent.setField(field)
			if agent.move(move):
				reward = agent.givereward()
			else:
				reward = 0

			record.append(reward)

		return max(enumerate(record),key=lambda x:x[1])
	else:
		record = []
		#for all the posible move 
		for move in actionTranslate:
			#set the field
			agent.setField(field)
			if agent.move(move):
				reward = agent.givereward()
				value_next = explore(agent.field, level-1)[1]
				value = reward + discount * value_next
			else:
				reward = 0
				value = reward

			record.append(value)
		return max(enumerate(record),key=lambda x:x[1])

class AIagent(object):
	def makeMove(self, field):
		bestSolution = explore(field,6)
		move = actionTranslate[bestSolution[0]]
		return move

	def makeMoveOnLevel(self, field, level):
		bestSolution = explore(field,level)
		move = actionTranslate[bestSolution[0]]
		return move

if __name__ == '__main__':
	game = GameAgent.GameField(height=4, width=4, win=2048)
	ai = AIagent()

	for level in range(2,9):

		record = []
		for times in range(500):
			game.reset()
			while (not game.is_win()) and (not game.is_gameover()):
				action = ai.makeMoveOnLevel(game.field, level)
				while not game.move(action):
					#it would have some unfeasible action, especilly when lv is small
					action = choice(actionTranslate)
			
			#take the record
			record.append((game.is_win(),game.score,game.highscore))
			print "result:",game.is_win(),"game score:",game.score,"highest score:",game.highscore

		#do some stats
		win_lose = [i[0] for i in record]
		win_rate = win_lose.count(True)
		avg_score = sum([i[1] for i in record]) / 500.0
		avg_highscore = sum([i[2] for i in record]) / 500.0

		sumup = {"record":record, "win_rate":win_rate, "avg_score":avg_score, "avg_highscore":avg_highscore}
		print "sum up:",sumup

		#write to file
		with open("level|"+level,"w") as f:
			json.dump(sumup,f)


