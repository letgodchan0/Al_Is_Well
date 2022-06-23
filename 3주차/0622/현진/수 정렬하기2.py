from collections import deque
from curses import nocbreak
import sys
input = sys.stdin.readline

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    cnt = 0

    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if cnt > 10:
                print(-1)
                return
            if maze[rx][ry] == 'O':
                print(cnt)
                return
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nrx, nry = rx, ry
                while True:
                    nrx += di
                    nry += dj
                    if maze[nrx][nry] == '#':
                        nrx -= di
                        nry -= dj
                        break
                    if maze[nrx][nry] == 'O':
                        break

                nbx, nby = bx, by
                while True:
                    nbx += di
                    nby += dj
                    if maze[nbx][nby] == '#':
                        nbx -= di
                        nby -= dj
                        break
                    if maze[nbx][nby] == 'O':
                        break
                if maze[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= di
                        nry -= dj
                    else:
                        nbx -= di
                        nby -= dj
                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
    print(-1)

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(input()))
    for j in range(M):
        if maze[i][j] == 'R':
            rx, ry = i, j
        elif maze[i][j] == 'B':
            bx, by = i, j
bfs(rx, ry, bx, by)