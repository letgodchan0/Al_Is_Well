def bfs(i, j, color):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] == color:
                visited[ni][nj] = 1
                q.append((ni, nj))
    return 1
    
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
color = ['R', 'B', 'G']
answer1 = 0
answer2 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] in color and visited[i][j] == 0:
            answer1 += bfs(i, j, arr[i][j])
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] in color and visited[i][j] == 0:
            answer2 += bfs(i, j, arr[i][j])
print(answer1, answer2)