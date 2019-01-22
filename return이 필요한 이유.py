a=10
def squre():
	b=a*a
	#return b #지역변수는 함수가 끝나면 값이 사라진다 그러므로 return으로 반환을 안해주면 전역변수로 쓸 수 없다
	
c=squre()+20