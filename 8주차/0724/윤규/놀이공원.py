n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))


if n <= m:
    print(n)
else:
    start = 0
    end = 60000000000
    while start <= end:
        mid = (start + end) // 2
        cnt = m
        for i in range(m):
            cnt += mid // arr[i]
        if cnt >= n:
            time = mid
            end = mid - 1
        else:
            start = mid + 1

    cnt2 = m
    for i in range(m):
        cnt2 += (time-1)//arr[i]
    
    for i in range(m):
        if time % arr[i] == 0:
            cnt2 += 1
        if cnt2 == n:
            print(i+1)
            break