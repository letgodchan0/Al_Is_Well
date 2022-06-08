# 회의실 배정
N = int(input())
arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))
meeting = sorted(arr, key=lambda x : (x[1], x[0]))

cnt = 1
final = meeting[0][1]
for i in range(1, N):
    if meeting[i][0] >= final:
        cnt += 1
        final = meeting[i][1]

print(cnt)