import sys
from collections import deque

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    visited[x][y] = 1
    check = [(x, y)]
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == '0':
                q.append((nx, ny))
                visited[nx][ny] = 1
                check.append((nx, ny))
    for i, j in check:
        grid[i][j] = check

n, m = map(int, input().split())
arr = [list(sys.stdin.readline().rstrip())for _ in range(n)]
visited = [[0] * m for _ in range(n)]
grid = [[1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == '0' and not visited[i][j]:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            lst = []
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and type(grid[ni][nj]) != int:
                    if grid[ni][nj] not in lst:
                        lst.append(grid[ni][nj])
            lst = list(map(lambda x : len(x), lst))
            arr[i][j] = str((sum(lst)+1)%10)

for a in arr:
    print(''.join(a))