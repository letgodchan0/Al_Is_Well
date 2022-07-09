import sys

n, m = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))

start = max(lst); end = sum(lst)
answer = sys.maxsize

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    check = 0

    for i in range(n):
        if check + lst[i] <= mid:
            check += lst[i]
        else:
            cnt += 1
            check = lst[i]

        if cnt > m:
            break
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        if mid >= max(lst):
            answer = min(answer, mid)
print(answer)
