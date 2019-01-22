board = ["6..874.1.",
		 "..9.36...",
		 "...19.8..",
		 "7946.....",
		 "..1.894..",
		 "...41..69",
		 ".7..5..9.",
		 ".539.76..",
		 "9.2.61.47",
]

def main():
	for idx,line in enumerate(board):
		board[idx]=list(line)
	cleanprint(board)
	print()
	solve()
	cleanprint(board)

def solve():
	while True:
		switch = False
		for i in range(0,9):
			for j in range(0,9):
				possibilities = getPossibilities(i,j)
				if possibilities == False:
					continue
				if len(possibilities)==1:
					board[i][j]=possibilities[0]
					switch = True
		if switch == False:
			break

def getPossibilities(i,j):
	if board[i][j]!='.':
		return False	
	possibilities = {str(n) for n in range(1,10)}
	possibilities -= set(board[i])
	for index in range(0,9):
		possibilities -= set(board[index][j])
	iStart = (i//3)*3
	jStart = (j//3)*3
	subboard = board[iStart:iStart+3]
	for index,ms in enumerate(subboard):
		subboard[index]=ms[jStart:jStart+3]
	for n in range(0,3):
		possibilities -= set(subboard[n])
	return list(possibilities)
	
def cleanprint(c):
	for a in c:
		for b in a:
			print(b,end='')
		print()
	
main()