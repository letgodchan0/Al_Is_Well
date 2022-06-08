# 두 동전
from collections import deque
import sys

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

def bfs(a, b, c, d):
    visited = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[a][b][c][d] = 0
    queue = deque([(a, b, c, d)])

    while queue:
        a, b, c, d = queue.popleft()
        if visited[a][b][c][d] >= 10:
            break

        for k in range(4):
            aa = a + di[k]
            bb = b + dj[k]
            cc = c + di[k]
            dd = d + dj[k]

            if not (0 <= aa < N and 0 <= bb < M) and not (0 <= cc < N and 0 <= dd < M):
                continue

            if not (0 <= aa < N and 0 <= bb < M):
                return visited[a][b][c][d] + 1
            if not (0 <= cc < N and 0 <= dd < M):
                return visited[a][b][c][d] + 1

            # 돌아갈 곳이 벽이면 제자리로
            if board[aa][bb] == '#':
                aa -= di[k]
                bb -= dj[k]
            if board[cc][dd] == '#':
                cc -= di[k]
                dd -= dj[k]

            if visited[aa][bb][cc][dd] == -1:
                visited[aa][bb][cc][dd] = visited[a][b][c][d] + 1
                queue.append((aa, bb, cc, dd))
    return -1

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
a, b, c, d = 0, 0, 0, 0
check = True

for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            if check:
                a, b = i, j
                check = False
            else:
                c, d = i, j

print(bfs(a, b, c, d))