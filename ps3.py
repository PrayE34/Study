board = ["4........",
		 ".........",
		 ".........",
		 ".........",
		 ".........",
		 ".........",
		 ".........",
		 ".........",
		 ".........",
]

def main():
	for idx,line in enumerate(board):
		board[idx]=list(line)
	cleanprint()
	print()
	easy()
	hard()
	cleanprint()
	
def easy():
	while True:
		switch = False
		for i in range(0,9):
			for j in range(0,9):
				maybe = possible(i,j)
				if maybe == False:
					continue
				if len(maybe)==1:
					board[i][j]=maybe[0]
					switch = True
		if switch == False:
			break
			
def hard():
	global board
	if complete():
		return True
	i,j=0,0
	for rowIdx,row in enumerate(board):
		for colIdx,col in enumerate(row):
			if col == '.':
				i,j = rowIdx,colIdx
	maybe = possible(i,j)
	for value in maybe:
		snapshot = copy.deepcopy(board)
		board[i][j] = value
		result = hard()
		if result == True:
			return True
		else:
			board = copy.deepcopy(snapshot)
	
def possible(i,j):
	global board
	if board[i][j]!='.':
		return False
	maybe = {str(n) for n in range(1,10)}
	maybe -= set(board[i])
	for index in range(0,9):
		maybe -= set(board[index][j])
	iStart = (i//3)*3
	jStart = (j//3)*3
	subboard = board[iStart:iStart+3]
	for index,ms in enumerate(subboard):
		subboard[index]=ms[jStart:jStart+3]
	for n in range(0,3):
		maybe -= set(subboard[n])
	return list(maybe)

def complete():
	for row in board:
		for col in row:
			if (col=="."):
				return False
	return True		
	
def cleanprint():
	for a in board:
		for b in a:
			print(b,end='')
		print()

import copy		
main()