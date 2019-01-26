road = [['.'],['.'],['.'],['.'],['.'],['.'],['.'],['.'],['.'],['.']]
for i in range(10):
	road[i]=list(input())

def main():
	print (road)
	print ()
	seek(1,1)
	clearprint()
	
def seek(i,j):
	while i<9 and j<9:
		if road[i][j]=='2':
			break
		elif road[i][j+1]=='1':
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
