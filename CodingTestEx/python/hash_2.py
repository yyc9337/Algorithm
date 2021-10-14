clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]


print(range(0, len(clothes)))

def solution(phone_book):
    for i in range(1,len(phone_book)) :    
        if phone_book[i].find(phone_book[0]) != -1 :
            return False
    return True



        


