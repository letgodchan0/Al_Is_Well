k, n = map(int, input().split(' '))
lan = []
for _ in range(k):
    lan.append(int(input()))

start = 1
end = sum(lan)//n

    
while start <= end:
    mid = (start + end)//2
    cnt = 0
    for i in range(k):
        cnt += lan[i]//mid
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1
    
print(end)
            