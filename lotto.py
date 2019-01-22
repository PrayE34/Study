#input('로또 번호를 선택해라 닝겐! ')

z=int(0)
y=int(0)

list1 = []	
list2 = []

for a in range (1,8):
	list1 = list1 + [int(input('1~60 사이의 숫자를 적어라 닝겐! '))]

for b in range (1,8):
	import random
	list2 = list2 + [random.randint(1,60)]
	
print (list1)
print (list2)

for a in range (1,7):
	if list1[a] in list2:
		z=z+1
if list2[6] in list1:
	y=y+1
	
print('맞은개수 : ',z)
print('보너스 개수 ',y)

if z == 6:
	print('1등')
elif z == 5 and y == 1:
	print('2등')
elif z == 5 and y == 0:
	print('3등')
elif z == 4:
	print('4등')
elif z == 3:
	print('5등')
else:
	print('다음 기회에')

