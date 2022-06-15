from collections import deque

def bfs(bx, by):
    while queue:
        x, y = queue.popleft()
        if arr[bx][by]=='S':
            return distance[bx][by]
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if nx in range(r) and ny in range(c):
                if (arr[nx][ny] == '.' or arr[nx][ny] == 'D') and arr[x][y] == 'S':
                    arr[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                elif (arr[nx][ny] =='.' or arr[nx][ny] =='S') and arr[x][y] == '*':
                    arr[nx][ny] = '*'
                    queue.append((nx,ny))
    return "KAKTUS"
            
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
distance=[[0]*c for _ in range(r)]
move=[(1,0),(0,1),(-1,0),(0,-1)]
queue = deque()

for i in range(r):
    for j in range(c):
        if arr[i][j]=='D':
            beaver_x = i
            beaver_y = j
        elif arr[i][j]=='S':
            queue.append((i, j))

for i in range(r):
    for j in range(c):
        if arr[i][j]=='*':
            queue.append((i, j))
#고슴도치가 먼저 이동하고 물이 차도록 함

print(bfs(beaver_x, beaver_y))