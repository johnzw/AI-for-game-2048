import GameAgent2
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

def makeMove(field):
	bestSolution = explore(field,6)
	move = actionTranslate[bestSolution[0]]
	return move

sample = [[0,0,0,0],
		  [0,2,0,4],
		  [2,0,0,0],
		  [2,0,0,0]]

print makeMove(sample)