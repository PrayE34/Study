#짝수행 날리기
import pandas as pd
df = pd.read_excel('data.xlsx')
df[::2].to_excel('even.xlsx')

#홀수행은?
df[1::2].to_excel('odd.xlsx')

#엑셀파일 읽기
import pandas as pd
df= pd.read_excel('a.xlsx', sheetname = 'Sheet1')
df

#엑셀파일 쓰기
df.to_excel('b.xlsx', sheet_name = 'Sheet1')