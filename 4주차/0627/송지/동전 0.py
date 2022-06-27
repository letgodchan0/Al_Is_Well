def find_mon(aim, much_lst):
    for i in range(len(much_lst)):
        
        if aim == 0:
            return 0
        else:
            for i in range(len(much_lst)):
                if much_lst[i] > aim:
                    imsi = aim // much_lst[i-1]
                    geum = imsi * much_lst[i-1]
                    break
                if much_lst[i] == much_lst[-1]:
                    imsi = aim // much_lst[i]
                    geum = imsi * much_lst[i]
                    break
            return imsi + find_mon(aim - geum, much_lst)


money, mok = map(int, input().split())
money_lst = [0 for i in range(money)]

for i in range(money):
    money_lst[i] = int(input())
    
print(find_mon(mok, money_lst))