# 데스 나이트
from collections import deque
import sys

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    chess[i][j] = 0

    while queue:
        i, j = queue.popleft()
        for di, dj in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and chess[ni][nj] == -1:
                queue.append((ni, nj))
                chess[ni][nj] = chess[i][j] + 1

input = sys.stdin.readline
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
chess = [[-1] * N for _ in range(N)]
bfs(r1, c1)

print(chess[r2][c2])