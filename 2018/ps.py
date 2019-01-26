import copy

'''board = ["6..874.1.",
		 "..9.36...",
		 "...19.8..",
		 "7946.....",
		 "..1.894..",
		 "...41..69",
		 ".7..5..9.",
		 ".539.76..",
		 "9.2.61.47",
]'''

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

#main 함수 설정
def main():
	#board를 리스트에 넣는다
	for idx,line in enumerate(board):
		board[idx]=list(line)
	#easy함수를 실행
	easy()
	hard()
	cleanprint()
	#print(getPossibilities(2,2))

#esay 함수 설정
def easy():
	global board
	#True면 계속 돌린다
	while True:
		#board에서 숫자가 바뀌지않으면 돌릴 필요가 없다
		switch = False
		#board 칸 하나하나 마다 경우의 수 검사
		for i in range(0,9):
			for j in range(0,9):
				possibilities = getPossibilities(i,j)
				#board에 .이 아닌 숫자가 있다면 그대로 진행한다(1)
				if possibilities == False:
					continue
				#경우의 수가 하나 남으면 정답이다
				if len(possibilities)==1:
					board[i][j]=possibilities[0]
					#board에서 숫자가 바뀌었다면 다시 돌려야하므로 True
					switch = True
		#True로 안바뀌고 False인 그대로라면 while을 나온다
		if switch == False:
			break
def hard():
	global board
	
	#완성했으니 할 일이 없다
	if complete():
		return True
	
	i,j=0,0
	for rowIdx,row in enumerate(board):
		for colIdx,col in enumerate(row):
			if col == '.':
				i,j = rowIdx,colIdx
				
	#경우의 수를 모두 불러온다
	possibilities = getPossibilities(i,j)
	#경우의 수 중 하나를 i,j에 넣어본다
	for value in possibilities:
		snapshot = copy.deepcopy(board)
		board[i][j] = value
		#함수 solve가 True(모두 채워졌다면)라면 끝
		result = hard()
		if result == True:
			return True
		else:
			board = copy.deepcopy(snapshot)
	
	

#getPossibilities 함수 설정 (i,j 고정)
def getPossibilities(i,j):
	global board
	#board에 .이 아닌 숫자가 있다면 그대로 진행한다(2)
	if board[i][j]!='.':
		return False
	#모든 경우의 수 호출 (현재 경우의 수 : 1~9)
	possibilities = {str(n) for n in range(1,10)}
	#가로 제외 
	possibilities -= set(board[i])
	#세로 제외
	for index in range(0,9):
		possibilities -= set(board[index][j])
	#네모 제외
	##3x3 으로 쪼갠다
	iStart = (i//3)*3
	jStart = (j//3)*3
	#세로 쪼개기
	subboard = board[iStart:iStart+3]
	#가로 쪼개기
	for index,ms in enumerate(subboard):
		subboard[index]=ms[jStart:jStart+3]
	##3x3 제외
	#for row in subboard:
	#	for col in row:
	#		possibilities -= set(col)
	for n in range(0,3):
		possibilities -= set(subboard[n])
	#리스트로 바꾼다
	return list(possibilities)

#board를 검사해서 끝났다면 True 안끝났으면 False라는 함수를 만든다
def complete():
	for row in board:
		for col in row:
			if (col=="."):
				#.이 남아있다면 미완성이니 False
				return False
	#.이 없다면 완성이니 True
	return True		
	
#깔끔하게 보이기
def cleanprint():
	for a in board:
		for b in a:
			print(b,end='')
		print()
	
main()