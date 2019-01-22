road = ["1111111111",
		"1001000001",
		"1001110001",
		"1002000101",
		"1000000101",
		"1000010001",
		"1000012001",
		"1000010021",
		"1000000001",
		"1111111111"
		]

def main():
	for idx,line in enumerate(road):
		road[idx]=list(line)
	seek(1,1)
	
def seek(i,j):
	while i<9 and j<9:
		if road[i][j]=='2':
			break
		elif road[i][j+1]=='1': #버그 리포트 : int로 if를 구성했으나 str 로 입력을 받아서 함수가 작동이 안됨
			road[i][j]='9'
			i=i+1
		elif road[i][j]=='0':
			road[i][j]='9'
			j=j+1
		
def clearprint():
	global road
	for i in road:
		for j in i:
			print(j,end='')
		print()
		
main()
clearprint()

#좌표 i,j
#j+1 = if 1 i+1 j로 간다 (혹시 아래도 1이면 종료),  if 0 j+1에 9표시, if 2 종료
#      if 

#print (road[1][1])