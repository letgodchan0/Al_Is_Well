n, m = map(int,input().split())
lessons = list(map(int,input().split()))
left = max(lessons)
right = sum(lessons)

#블루레이의 크기를 이분탐색으로 찾아가기
while left<=right:
    mid = (left + right)//2

    bluray, minute = 0, 0   #블루레이 개수, 시간
    for i in range(n):
        if minute + lessons[i] > mid:
            bluray += 1
            minute = 0
        minute += lessons[i]
    if minute:
        bluray += 1 

    if bluray <= m:
        right = mid - 1
    else:
        left = mid + 1

print(left)