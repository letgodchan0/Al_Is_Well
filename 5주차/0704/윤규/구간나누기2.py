n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))



def divide(x):
    maxV = arr[0]
    minV = arr[0]
    cnt = 1
    for i in range(1, n):
        maxV = max(maxV, arr[i])
        minV = min(minV, arr[i])
        if maxV - minV > x:
            cnt += 1
            maxV = arr[i]
            minV = arr[i]
    return cnt


res = 0
start = 0
end = max(arr)



while start <= end:
    mid = (start + end) // 2
    if divide(mid) > m:
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)