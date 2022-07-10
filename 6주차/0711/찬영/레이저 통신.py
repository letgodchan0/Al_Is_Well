import sys
from collections import deque
input = sys.stdin.readline
big = sys.maxsize
def bfs(x, y):
    q = deque([])
    visited = [[big] * w for _ in range(h)]
    q.append((x, y, 0, 0, 0))
    visited[x][y] = 0

    while q:
        x, y, cnt, direction_x, direction_y = q.popleft()
        if x == e1 and y == e2:
            return cnt

        if visited[x][y] < cnt:
            continue

        visited[x][y] = cnt

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '*':

                if (direction_x == 0 and direction_y == 0) or (direction_x == dx and direction_y == dy):
                    q.appendleft((nx, ny, cnt, dx, dy))
                else:
                    q.append((nx, ny, cnt+1, dx, dy))

w, h = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(h)]
idx = []
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            idx.append((i, j))
    if len(idx) == 2:
        break

s1, s2 = idx[0]
e1, e2 = idx[1]
res = bfs(s1, s2)
print(res)