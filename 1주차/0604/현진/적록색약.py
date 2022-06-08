# 적록색약
def bfs(i, j):
    queue = []
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        i, j = queue.pop(0)
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and grid[ni][nj] == grid[i][j]:
                visited[ni][nj] = 1
                queue.append((ni, nj))

N = int(input())
grid = [list(input()) for _ in range(N)]

# 적록색약이 아닌 사람의 경우
RGB_cnt = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            RGB_cnt += 1

# 적록색약인 사람의 경우
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

RRB_cnt = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            RRB_cnt += 1

print(RGB_cnt, RRB_cnt)