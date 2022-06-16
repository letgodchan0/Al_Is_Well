n = int(input())
now = list(map(int, input()))
want = list(map(int, input()))
ans = -1

def switch(now):
    cnt = 1
    now[0], now[1] = (now[0] + 1) % 2, (now[1] + 1) % 2
    for i in range(1, len(now)):
        if now[i-1] == want[i-1]:
            continue
        else:
            cnt += 1
            now[i-1], now[i] = (now[i-1] + 1) % 2, (now[i] + 1) % 2
            if i < len(now)-1:
                now[i+1] = (now[i+1] + 1) % 2
    if now == want:
        return cnt
    return 100001

def notswitch(now):
    cnt = 0

    for i in range(1, len(now)):
        if now[i-1] == want[i-1]:
            continue
        else:
            cnt += 1
            now[i-1], now[i] = (now[i-1] + 1) % 2, (now[i] + 1) % 2
            if i < len(now)-1:
                now[i+1] = (now[i+1] + 1) % 2
    if now == want:
        return cnt
    return 100001

cnt = min(switch(now[:]), notswitch(now[:]))
if cnt == 100001:
    cnt = -1
print(cnt)


