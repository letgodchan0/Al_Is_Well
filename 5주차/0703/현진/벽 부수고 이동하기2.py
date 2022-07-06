# 시간초과 
from collections import deque
from sys import stdin

input = stdin.readline

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[0][0] = [1] * (K + 1)

    while queue:
        # 좌표와 벽을 부술 수 있는 남은 횟수
        i, j, c = queue.popleft()
        if i == N - 1 and j == M - 1:
            return visited[i][j][c]
        nextVisited = visited[i][j][c] + 1

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj][c]:
                # 빈 방이라면
                if not arr[ni][nj]:
                    visited[ni][nj][c] = nextVisited
                    queue.append([ni, nj, c])
                # 벽을 아직 부술 수 있다면
                elif c < K:
                    visited[ni][nj][c + 1] = nextVisited
                    queue.append([ni, nj, c + 1])
    return -1

N, M, K = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

print(bfs())