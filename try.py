#if clothes[0][1] in clothes[1,2,3,4,5,6...][1]
'''

#뒤에 원소와 비교하고 카운트 올리기 & 해당 리스트 삭제
clothes = [["crow_mask", "face"], 
["blue_sunglasses", "face"], 
["smoky_makeup", "face"],
["yellow_hat", "headgear"], 
["blue_sunglasses", "eyewear"], 
["green_turban", "headgear"]]

for i in range (len(clothes)):
	clothes[i][0],clothes[i][1] = clothes[i][1],clothes[i][0]

clothes.sort()

i=0
while len(clothes[i:])>1:
	if clothes[i][0] == clothes[i+1][0]:
		clothes[i] = clothes[i]+clothes[i+1]
		del clothes[1]
	else:
		i+=1
		

	print(clothes)
	print(len(clothes))
			
			
for i in range (len(clothes)):
	change += set(clothes[i])
	print(i)
	print (change)






for i in range(len(clothes)):
	for j in range(len(clothes)-i):
		if clothes[i][1] == clothes[i+j+1][1]:
			clothes[i] = clothes[i]+clothes[i+j+1]
			del clothes[i+j+1]
		print(clothes[i])
		print(clothes)
		print()
		
		
for j in range(len(clothes)-1):
	if clothes[0][1] == clothes[1][1]:
		clothes[0] = clothes[0]+clothes[j+1]
		del clothes[j+1]
	print(clothes[0])
print(clothes)
print()

clothes = [["crow_mask", "face"], 
["blue_sunglasses", "face"], 
["smoky_makeup", "face"],
["yellow_hat", "headgear"], 
["blue_sunglasses", "eyewear"], 
["green_turban", "headgear"]]



for i in range (len(clothes)):
	clothes[i][0],clothes[i][1] = clothes[i][1],clothes[i][0]

clothes.sort()
print(clothes)

a=0 #같은 묶음의 개수

while len(clohtes)>a:
	if list[a][0]==list[a+1][0]
		list[a]+=list[1]
		del list[1]
	else
		a+=1
		break
'''
clothes = [["crow_mask", "face"], 
["blue_sunglasses", "face"], 
["smoky_makeup", "face"],
["yellow_hat", "headgear"], 
["blue_sunglasses", "eyewear"], 
["green_turban", "headgear"]]

list1=[0]

for i in range(len(clothes)-1):
	if clothes[0][1] == clothes[i+1][1]:
		list1.append(i+1)
print(list1)
print(clothes)
for j in range(len(list1)):
	del clothes[j]
print(list1)
print(clothes)


		
		
		












		
#list 같으면 인덱스 값

























