import sys
def dfs(i, j, cnt, total):
    global result
    if result >= total + (4 - cnt) * max_value:
        return
    if cnt == 4:
        result = max(result, total)
        return
    else:
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if cnt == 2:
                    visited[ni][nj] = 1
                    dfs(i, j, cnt+1, total+arr[ni][nj])
                    visited[ni][nj] = 0
                visited[ni][nj] = 1
                dfs(ni, nj, cnt+1, total+arr[ni][nj])
                visited[ni][nj] = 0

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = 0
max_value = max(map(max, arr))
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0
print(result)