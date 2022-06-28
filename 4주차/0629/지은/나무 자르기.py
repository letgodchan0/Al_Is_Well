n, m = map(int,input().split())
trees = list(map(int,input().split()))
l, r = 0, max(trees)    #절단기에 높이의 시작과 끝

while l<=r:             #이분탐색
    mid = (l+r)//2

    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total == m:
        answer = mid
        break
    if total > m:
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)