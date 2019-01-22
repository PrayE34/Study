'''
x=7
x=x+1
x=int(x/2)


for abc in range (1,7):  #1 ~ 6
	for deg in range (1,abc): #1 ~ abc-1
		print('*',end='')
	print()
	
for a in range (x,-1,-1): #x~0 --1
	for aa in range (a-1,0,-1): #a-1 ~ 1 --1
		print(" ",end='')
		for b in range (1,x+1): #1~x
			for bb in range (1,2*x,2): #1~2x-1 ++2
				print("*",end='')
		print()
	
for a in range (7,-1,-1): #7~0 -1씩 감소
	print (a)

	
x = 7
for i in range(1,x+1):
	for j in range(i):
		print('*',end='')
	print()
print()
	
	
	
for i in range(1,x+1):
	for j in range(x-i):
		print(' ',end='')
	for j in range (i):
		print('*',end='')
	print()
print()



for i in range(1,x+1):
	for j in range(x+1-i):
		print(' ',end='')
	for j in range(2*i-1):
		print('*',end='')
	print()
	'''
	

x=int(input('숫자를 적어주세요 : '))

x=int(x+1)
x=int(x/2)	
	
for i in range (1,x+1):
	for j in range (x-i):
		print(" ",end='')
	for j in range (2*i-1):
		print("*",end='')
	print()

x=int(x-1)

for i in range (x,0,-1):
	for j in range (x+1-i):
		print(' ',end='')
	for j in range (2*i-1):
		print('*',end='')
	print()


x=int(input('숫자를 넣어라 닝겐!! '))
y=(x+1)//2

for i in range (1-y,x+1-y):
	if i<0:
		i=i*-1
	for j in range (i):
		print(' ',end='')
	for j in range (x-2*i):
		print('*',end='')
	print()








	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
