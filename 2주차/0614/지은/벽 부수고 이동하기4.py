#각 그룹별로 0의 개수가 몇개인지 딕셔너리로 저장
#상하좌우 인접한 그룹을 구하고 그 그룹에 해당하는 0의 개수 더해준다

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        i, j = q.popleft()
        zeros[i][j] = group
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if ni not in range(n) or nj not in range(m) or visited[ni][nj] or graph[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            q.append((ni, nj))
            cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
group = 1
info = {}
info[0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):     
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1

for i in range(n):
    for j in range(m):
        addList = set()
        if graph[i][j]:
            for idx in range(4):
                ni, nj = i + dy[idx], j + dx[idx]
                if ni not in range(n) or nj not in range(m):
                    continue
                addList.add(zeros[ni][nj])
            for add in addList:
                graph[i][j] += info[add]
                graph[i][j] %= 10

for g in graph:
    print("".join(map(str, g)))