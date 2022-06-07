"""
r좌표와 c좌표가 있다.
데스 나이트가 이동할 수 있는 범위는 다음과 같다. 
(c -= 2), (c += 2), (r -= 2, c -= 1), (r -= 2, c += 1), (r += 2, c -= 1), (r += 2, c += 1)

데스 나이트의 좌표 r1, c1이 주어질 때, r2, c2로 이동하는 최소 이동횟수를 구하라
단, 체스판의 크기는 N*N이며, 0~N-1 까지 존재하고, 체스판 밖으로는 이동할 수 없다.1

최단 경로이므로, BFS로 탐색하자.
"""
from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    chessboard[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and chessboard[ny][nx] == -1:
                q.append((ny, nx))
                chessboard[ny][nx] = chessboard[y][x] + 1

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
d = [(0, -2), (0, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]   # 이동 범위
chessboard = [[-1] * N for _ in range(N)]
bfs(r1, c1)
result = chessboard[r2][c2]
print(result)