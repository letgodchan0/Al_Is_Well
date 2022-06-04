def bfs(r, c):
    dk = deque()
    dk.append((r, c))
    chess[r][c] = 0 #시작점

    while dk:
        r, c = dk.popleft()

        for dr, dc in move:
            nr = r + dr
            nc = c + dc
            if nr in range(n) and nc in range(n) and chess[nr][nc]==-1: #범위 안에 있고 방문한 적 x
                dk.append((nr, nc))
                chess[nr][nc] = chess[r][c] + 1

from collections import deque

n = int(input())    #체스판의 크기
r1, c1, r2, c2 = map(int, input().split()) #r1,c1: 현재 위치 r2, c2: 목적지
move = [(-2,-1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

chess = [[-1]*n for _ in range(n)]   #체스판

bfs(r1,c1)
print(chess[r2][c2])




