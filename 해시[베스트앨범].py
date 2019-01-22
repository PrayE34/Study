def solution(genres, plays):
    dic = {}
    #장르별 점수표
    dik = []
    #개인 점수표 = 장르별 점수표 + 개인 점수 (총점수, 인덱스)
    answer = []
    
    for i,v in enumerate(plays):
        if genres[i] in dic:
            dic[genres[i]]+=v
        else:
            dic[genres[i]] = v
        dik.append([v,i])
   
    for i in range(len(genres)):
        dik[i][0] += dic[genres[i]]*10000
               
    dik.sort(reverse=True)
       
    for i in range(len(plays)):
        answer.append(dik[i][1])
    return answer
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
def solution(genres, plays):
    dic = {}
    #장르별 점수표
    dik = {}
    #개인 점수표 = 장르별 점수표 + 개인 점수 (장르, 인덱스)
    dib = []
    #장르 점수 비교용 리스트
    answer = []
    
    for i,v in enumerate(plays):
        #print(genres[i])
        if genres[i] in dic:
            dic[genres[i]]+=v
        else:
            dic[genres[i]] = v
    
    #for i in range(len(genres)):       
        #dik[genres[i]]=plays[i]
        #print(dic[genres[i]])
    #print(dik)
    
        
    
    #print(dic)
    #b= sorted(dic,reverse=True,key=lambda k : dic[k])
    #print(b)
    
    
    #b= sorted(dic)
    #print(b)
    #a=list(dic.items())
    #print(a)
    #dib.append([재생횟수,장르])
    
    
    #print(dic)
    #print(dik)
    
    #for i in range(len(genres)):
        #dik[i][0] += dic[genres[i]]
        #print(dik[i])
        #print(dic[genres[i]])
        #print(dic)
        #print(dik)
        
    #dik.sort(reverse=True)
    #print(dik)
    
    #for i in range(4):
        #answer.append(dik[i][1])
    #return answer
    
    did={}
    for i in range(5):
        did[i] = [dic[genres[i]],plays[i]]
    d = sorted(did,reverse=True,key=lambda k : did[k])
    print(did)
    print(d)
    return d
	
genres = ["classic", "pop", "classic", "classic", "pop"], 
plays=[500, 600, 150, 800, 2500]	
	
dic = {}
for i in range(len(plays)):
	if genres[i] in dic:
		dic[genres[i]]=dic[genres[i]]+[play[i]]
	else:
		dic[genres[i]]=[play[i]]
		
print (dic)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
