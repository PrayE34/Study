list1 = ["a","b","c","d","a","e","f","a","b","c"]
list2 = ["a","e","f"]
list3 = []

for i in range(len(list1)):
    #print(i)
    #print(list2.count(list1[i]))
    #print(list2.count(list1[i]))

    if list2.count(list1[i])==0:
        list3.append(list1[i])

    if list2.count(list1[i])>=1:
        list2.remove(list1[i])



    #if list2.count(list1[i])==0:
    #    list3.append(list1[i])

    #print(list3)
    #print(list2)
    #print(list1)

#elif list2.count(list1[i])==1:
    #    del list2[list1[i]]


	#
    #else:
    #    print()
    #print(list1[i])
print(list3)
#print(list2)
#print(list1)


 #else:
    #elif list2.count(list1[i])==0:
		#del list2[list1[i]]
    #    print("a")
	
	
	
	
	
'''def solution(participant, completion):
    list3=[]
    for i in range(len(participant)):
        if completion.count(participant[i])==0:
            list3.append(participant[i])
        if completion.count(participant[i])>=1:
            completion.remove(participant[i])
    for i in range(len(list3)):
        answer = list3[i]
    return answer'''
   
    
def solution(participant, completion):
    while len(completion)>=1:
        participant.remove(completion.pop(0))
    for i in range (len(participant)):
        answer = participant[i]
    return answer
	
def solution(participant, completion):
    while len(completion)>=1:
        participant.remove(completion.pop(0))
    for i in range (len(participant)):
        return participant[i]
        