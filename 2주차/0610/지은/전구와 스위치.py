n = int(input())
now = list(map(int, input())) #0: 켜짐 1: 꺼짐
hope = list(map(int, input())) 

#이전 전구의 상태가 희망 상태와 다를 경우 스위치를 누른다.
#지나간 전구는 다시 누르지 않는다

#첫번째 전구를 켠다
def push_first(now):
    cnt1 = 1
    now[0] = 1 - now[0] 
    now[1] = 1 - now[1]

    for i in range(1, len(now)):
        if now[i-1]==hope[i-1]:
            continue
        else:
            cnt1 += 1
            if i<len(now)-1:
                now[i-1], now[i], now[i+1] = 1-now[i-1], 1-now[i], 1-now[i+1]
            else:
                now[i-1], now[i] = 1-now[i-1], 1-now[i]

    if now != hope:
        cnt1 = 100001

    return cnt1

#첫번째 전구를 켜지 않는다
def not_push_first(now):
    cnt2 = 0

    for i in range(1, len(now)):
        if now[i-1]==hope[i-1]:
            continue
        else:
            cnt2 += 1
            if i<len(now)-1:
                now[i-1], now[i], now[i+1] = 1-now[i-1], 1-now[i], 1-now[i+1]
            else:
                now[i-1], now[i] = 1-now[i-1], 1-now[i]
        
    if now != hope:
        cnt2 = 100001

    return cnt2

mini = min(push_first(now[:]), not_push_first(now[:]))  #리스트를 복사하여 사용
print(mini if mini!=100001 else -1) #불가능: -1