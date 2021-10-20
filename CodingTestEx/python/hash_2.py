phone_book = ["119", "97674223", "1195524421"]


def solution(phone_book):
    for i in range(1,len(phone_book)) :    
        if phone_book[i].find(phone_book[0]) != -1 :
            return False
    return True



        


