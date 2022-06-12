from collections import deque

def bfs(x, y, water):
    q = deque([])
    q.append((x, y, 0))
    visited = [[0] * c for _ in range(r)]
    visited[x][y] =1
    visited2 = [[0] * c for _ in range(r)]
    for w1, w2, tmp in water:
        visited2[w1][w2] = 1

    while q:
        x, y, cnt = q.popleft()
        if arr[x][y] == 'D':
            return cnt

        if water:
            while water[0][-1] == cnt:
                w1, w2, time = water.pop(0)
                for dw1, dw2 in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nw1, nw2 = w1 + dw1, w2 + dw2
                    if 0 <= nw1 < r and 0 <= nw2 < c and arr[nw1][nw2] != 'D' and arr[nw1][nw2] != 'X' and not visited2[nw1][nw2]:
                        arr[nw1][nw2] = '*'
                        visited2[nw1][nw2] = 1
                        water.append((nw1, nw2, time+1))
                if not water:
                    break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != '*' and arr[nx][ny] != 'X' and not visited[nx][ny]:
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = 1

    return 'KAKTUS'

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

water = []
w1, w2 = -100, - 100
for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            water.append((i, j, 0))
        if arr[i][j] == 'S':
            s1, s2 = i, j

print(bfs(s1, s2, water))
