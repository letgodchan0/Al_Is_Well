"""
종료시간과 시작시간의 맞아떨어지는 것이 중요
종료시간 우선정렬 - 시작시간 후순위정렬
"""


N = int(input())
meetings = []
for i in range(N):
    start, end = map(int, input().split())
    meetings.append([start, end])

sorted_meetings = sorted(meetings, key = lambda x: (x[1], x[0]))
cnt = 1
end_time = sorted_meetings[0][1]

for i in range(1, N):
    if end_time <= sorted_meetings[i][0]:
        end_time = sorted_meetings[i][1]
        cnt += 1

print(cnt)