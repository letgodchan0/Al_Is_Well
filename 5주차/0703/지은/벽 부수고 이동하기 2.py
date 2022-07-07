from collections import deque

def bfs(i, j):
    position = deque()
    position.append((i, j, 0))
    visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
    visited[i][j][0] = 1
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    while position:
        i, j, wall = position.popleft()
        if i==n-1 and j==m-1:
            return visited[i][j][wall]
        for di, dj in move:
            ni = i + di
            nj = j + dj
            if 0<=ni<n and 0<=nj<m and visited[ni][nj][wall]==0:
                if arr[ni][nj]==1 and wall <= k:
                    visited[ni][nj][wall+1] = visited[i][j][wall]+1
                    position.append([ni, nj, wall+1])                    
                elif arr[ni][nj]==0:
                    visited[ni][nj][wall] = visited[i][j][wall]+1
                    position.append([ni, nj, wall])
    return -1

n, m, k = map(int, input().split())
arr = [list(map(int,list(input()))) for _ in range(n)]
print(bfs(0, 0))