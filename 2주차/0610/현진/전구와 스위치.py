# 전구와 스위치

def change(num):
    if num == 0:
        num = 1
    else:
        num = 0
    return num

def switch(bulb, cnt):
    count = cnt
    if count == 1:
        bulb[0] = change(bulb[0])
        bulb[1] = change(bulb[1])
    
    for i in range(1, N):
        if bulb[i - 1] != want[i - 1]:
            count += 1
            bulb[i - 1] = change(bulb[i - 1])
            bulb[i] = change(bulb[i])
            if i != N-1:
                bulb[i + 1] = change(bulb[i + 1])
    if bulb == want:
        return count
    else:
        return -1

N = int(input())
bulb = list(map(int, input().rstrip('\n')))
want = list(map(int, input().rstrip('\n')))

result1 = switch(bulb[:], 0)
result2 = switch(bulb[:], 1)

if result1 >= 0 and result2 >= 0:
    print(min(result1, result2))
elif result1 >= 0 and result2 < 0:
    print(result1)
elif result1 < 0 and result2 >= 0:
    print(result2)
else:
    print(-1)