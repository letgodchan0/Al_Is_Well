from collections import deque


N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = list(input())
visited = [[False] * N for _ in range(N)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(y, x, color):
    q = deque()
    q.append([y, x])

    while q:
        tmp = q.popleft()
        y = tmp[0]
        x = tmp[1]

        if visited[y][x] == False:
            visited[y][x] = True
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if arr[ny][nx] == color:
                        q.append([ny, nx])

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j, arr[i][j])
            cnt += 1

print(cnt, end=" ")

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j, arr[i][j])
            cnt += 1

print(cnt)