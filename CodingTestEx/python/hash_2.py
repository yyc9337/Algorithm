phone_book = ["119", "97674223", "1195524421"]


aa = phone_book[2].find(phone_book[0])

i = 0
while range(len(phone_book))  :
    i = i + 1
    if phone_book[i].find(phone_book[0]) != 0 :
        print(True)
        break
    else :
        print(False)    





