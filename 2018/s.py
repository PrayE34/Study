a=int(input())
for b in range(1,a+1):
    for i in range(a-b,0,-1):
        print(' ',end='')
    for j in range(1,b+1):
		print('*',end='')
	print()
