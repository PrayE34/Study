def f(n):
	if n==1:
		return 1
	else: 
		f(n-1)

#n=input("숫자를 입력해주세요")
#f(n)
print(f(3))