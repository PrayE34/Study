#웹소스 가져와서 출력하기
import requests

#특정 URL에 접속하는 요청(Request)객체를 생성합니다
request=requests.get('http://www.dowellcomputer.com/main.jsp')

#접속한 이후의 웹 사이트 소스코드를 추출합니다
html = request.text

print (html)
'''request 에서 s 안붙여서 버그
.을 ,로 잘못써서 버그'''


#뷰티풀수프
import requests
from bs4 BeatifulSoup

#특정 URL에 접속하는 요청(Request)객체를 생성합니다
request=requests.get('http://www.dowellcomputer.com/main.jsp')

#접속한 이후의 웹 사이트 소스코드를 추출합니다
html=request.text

#HTML 소스코드를 파이썬 객체로 변환합니다
soup = BeatifulSoup(html, 'html.parser')

#<a> 태크 포함하는 요소를 추출합니다
links=soup.select('td>a')

#모든 링크에 하나씩 접근합니다
for link in links:
	#링크가 href 속성을 가지고 있다면
	if link.has_attr('href'):
		#href 속성의 값으로 notice라는 문자열이 포함되어 있다면
		if link.et('href').find('notice') != -1:
			print(link.txt)

''' if 뒤에 : 안붙여서 버그
인터넷 주소 잘못써서 버그'''
