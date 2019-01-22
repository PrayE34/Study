def solution(clothes):
    
    List=[]
    dic={}
    c=1
    
    for i in range(len(clothes)):
        List.append(clothes[i][1])
        if List[i] in dic:
            dic[List[i]]+=1
			#딕셔너리는 value에서 연산가능
        else:
            dic[List[i]]=2
    for a,b in enumerate(dic.values()):
        c=c*b
    return(c-1)
	
	
import collections

def solution(clothes):
    tmp=1
    b=collections.Counter(list(clothes[i][1] for i in range(len(clothes))))
    for i,v in enumerate(b.values()):
        tmp*=v+1
    return (tmp-1)