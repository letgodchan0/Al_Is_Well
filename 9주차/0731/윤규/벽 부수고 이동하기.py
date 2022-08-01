
from collections import deque


n, m = map(int, input().split(' '))
arr = [list(map(int, input(''))) for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[[n*m + 1] * 2 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1

while q:
    
    i, j, cnt = q.popleft()
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] == 0:
                if visited[ni][nj][cnt] > visited[i][j][cnt] + 1: 
                    q.append((ni, nj, cnt))
                    visited[ni][nj][cnt] = visited[i][j][cnt] + 1
                
            elif arr[ni][nj] == 1 and cnt == 0:
                if visited[ni][nj][cnt + 1] > visited[i][j][cnt] + 1:
                    q.append((ni, nj, cnt+1))
                    visited[ni][nj][cnt + 1] = visited[i][j][cnt] + 1
                

if min(visited[n-1][m-1]) == n*m+1:
    print(-1)
else:
    print(min(visited[n-1][m-1]))



