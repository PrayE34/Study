#copy 함수 도입
import copy

board = ["4........",
		 "..3......",
		 "9...1.8..",
		 ".........",
		 ".........",
		 "..7......",
		 ".........",
		 ".........",
		 ".........",
]
#board를 리스트에 넣기
def main():
	global board
	for idx,line in enumerate(board):
		board[idx]=list(line)
#solve함수로 문제 풀기
	solve()
	printBoard()
	#print(getPossibilities(2,2))
	
'''#solve 함수 만들기
def solve():
	global board
	##칸마다 가능한 숫자 계산
	###세로
	for i in range(0,9):
		###가로
		for j in range(0,9):
			###9x9 칸마다 가능한 경우의 수 계산
			possibilities = getPossibilities(i,j)
			###하나만 남으면 정답이다
			if len(possibilities) == 1:
				board[i][j]=possibilities[0]'''
				
#getPossibilities 함수 만들기 (고정변수 : i,j)
def getPossibilities(i,j):
	global board
	#board 가 .이 아닌 숫자로 채워져있을 때
	if board[i][j] != ".":
		return False
	
	#칸마다 가능한 총 경우의 수 (집합을 사용 : 집합은 반복해서 빼거나 없는걸 빼도 오류가 안난다)
	possibilities = {str(n) for n in range(1,10)}
	
	#가로 겹치는 숫자를 제외시킨다 ex)board[1]=..1..5... -> 1,5 제외(.은 없기때문에 그냥 진행해버림)
	for val in board[i]:
		possibilities -= set(val)
	
	#세로 겹치는 숫자를 제외시킨다 ex)board[0~8][1]=..2..9... -> 2,9 제외(.은 없기때문에 그냥 진행해버
	for idx in range(0,9):
		possibilities -= set(board[idx][j]) # -----------가로 안닫아서 오류
		
	iStart = (i//3)*3
	jStart = (j//3)*3
	
	#세로 3등분
	subboard = board[iStart:iStart+3]
	
	#가로 3등분
	for idx,row in enumerate(subboard):
		subboard[idx] = row[jStart:jStart+3]
	
	#subboard 안에 겹치는 숫자를 제외시킨다 : 2차원 배열(for문 2번 사용)
	for row in subboard:
		for col in row:
			possibilities -= set(col)
			
	return list(possibilities)
		
		
'''#solve 함수 만들기
def solve():
	global board
	##칸마다 가능한 숫자 계산
	###세로
	for i in range(0,9):
		###가로
		for j in range(0,9):
			###9x9 가능한 숫자 계산
			possibilities = getPossibilities(i,j)
			###+board 가 .이 아닌 숫자로 채워져있을 때
			if possibilities == False: #-----------false 소문자로 써서 오류
				continue
			###하나만 남으면 정답이다
			if len(possibilities) == 1:
				board[i][j]=possibilities[0]'''
				
#solve 함수 만들기
def solve():
	global board
	
	try:
		fillAllObvius()
	except:
		return False
		
	#fillAllObvius()
	# 일단 True로 받아준다
	if isComplete():
		return True
		
	i,j=0,0	
	for rowIdx,row in enumerate(board):
		for colIdx,col in enumerate(row):
			if col == '.':
				i,j=rowIdx, colIdx
				
	possibilities=getPossibilities(i,j)
	#경우의 수를 하나씩 집어넣어봅니다(1)
	for value in possibilities:
		#save
		snapshot = copy.deepcopy(board)
		#경우의 수를 하나씩 집어넣어봅니다(2)
		board[i][j] = value
		result = solve()
		#True가 아니라면 RollBack
		if result == True:
			return True
		else:
			#load
			board=copy.deepcopy(snapshot)
			
	return False		
		
#fillAllObvius함수 만들기		
def fillAllObvius():
	global board
	#조건이 참이라면 while은 계속 돌아간다
	while True:
		#board에 숫자가 채워지지않는 이상 다시 돌리는건 무의미하다
		somethingChange = False
		##칸마다 가능한 숫자 계산
		###세로
		for i in range(0,9):
			###가로
			for j in range(0,9):
				###9x9 가능한 숫자 계산
				possibilities = getPossibilities(i,j)
				###+board 가 .이 아닌 숫자로 채워져있을 때
				if possibilities == False: #-----------false 소문자로 써서 오류
					continue
				###만약 경우의 수가 하나도 안남는다면	
				if len(possibilities)==0:
					raise RuntimeError("No moves Left")
				###하나만 남으면 정답이다
				if len(possibilities) == 1:
					board[i][j]=possibilities[0]
					#정답이 나왔다는 것은 또 solve함수를 돌렸을 때, 사라질 경우의 수가 존재한다는 것이다 
					somethingChange = True
					
			#거짓이 나왔을 경우, 연산을 끝낸다(break도 상관없을 듯)
			if somethingChange == False:
				return

#깔끔한 도출을 위해 정리
def printBoard():
	global board
	for row in board:
		for col in row:
			print(col,end = '')
		print()

#isComplete함수 만들기		
def isComplete():
	for row in board:
		for col in row:
			#.이 남아있다면 False
			if (col == '.'):
				return False
				
	return True
main()