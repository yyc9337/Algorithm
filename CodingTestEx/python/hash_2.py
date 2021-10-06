phone_book = ["119", "97674223", "1195524421"]


aa = phone_book[1].find(phone_book[0])

print(aa)


def solution(phone_book):
    i = 0
    for i in range(len(phone_book)) :
        if phone_book[i].find(phone_book[0]) == 0 :
            return False
        else  :
            return True 
        
    answer = True

    return answer

print(solution(phone_book))