n = int(input())
meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda time:time[0])    #시작시간 순으로 정렬
meetings.sort(key=lambda time:time[1])    #종료시간 순으로 정렬
#종료 시간 순으로 정렬하되 종료시간이 같은 경우 시작 시간 순으로 정렬
#시작시간 정렬 안해주면 [[12, 12], [10, 12], [11, 12]]의 경우 틀린다

cnt, end = 0, 0
for meeting in meetings:
    if end <= meeting[0]:   #앞팀 끝나는 시간이 회의시작되는 시간보다 빠르면
        end = meeting[1]    #회의를 잡는다. 끝나는 시간을 회의가 끝나는 시간으로
        cnt += 1

print(cnt)

