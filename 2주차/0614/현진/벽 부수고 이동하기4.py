from collections import deque
import sys
from tokenize import group
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    cnt = 1
    while queue:
        i, j = queue.popleft()
        zeros[i][j] = group
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj] or graph[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            queue.append((ni, nj))
            cnt += 1
    return cnt

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
zeros = [[0] * M for _ in range(N)]
group = 1
info = {}
info[0] = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1

for i in range(N):
    for j in range(M):
        addList = set()
        if graph[i][j]:
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni = i + di
                nj = j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                addList.add(zeros[ni][nj])
            for add in addList:
                graph[i][j] += info[add]
                graph[i][j] %= 10

for i in graph:
    print(''.join(map(str, i)))