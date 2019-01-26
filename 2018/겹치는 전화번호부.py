#phone_book = [12124124,13231525,437624623,2,5234324,234,12,125,25,12,125,]
phone_book = ["113", "12340", "123440", "12345", "98346"]
phone_book.sort()

for i in range (len(phone_book)):
    for j in range(len(phone_book)-i-1):

        if phone_book[i]==phone_book[i+j+1][0:len(phone_book[i])]:
            print("True")
            print(i)
            print (j)
            print(phone_book[i])
            print(phone_book[i+j+1][0:len(phone_book[i])])
            print(phone_book[i + j+1])
            print()
        else:
            print("flase")
            print(i)
            print (j)
            print(phone_book[i])
            print(phone_book[i + j+1][0:len(phone_book[i])])
            print(phone_book[i + j+1])
			
			
			
			
def solution(phone_book):
    phone_book.sort()

    for i in range (len(phone_book)):
        for j in range(len(phone_book)-i-1):
            if phone_book[i]==phone_book[i+j+1][0:len(phone_book[i])]:
                return False
            else:
                return True