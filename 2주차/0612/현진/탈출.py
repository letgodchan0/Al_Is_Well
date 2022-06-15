from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue.append([x, y])
    visited[x][y] = 1
    while queue:
        queueLength = len(queue)
        while queueLength:
            x, y = queue.popleft()
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])
                    elif graph[nx][ny] == 'D':
                        print(visited[x][y])
                        return
            queueLength -= 1
        waterBfs()
    print('KAKTUS')
    return

def waterBfs():
    waterLength = len(water)
    while waterLength:
        x, y = water.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    water.append([nx, ny])
        waterLength -= 1
            
N, M = map(int, input().split())

graph = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
queue, water = deque(), deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'S':
            x1, y1 = i, j
            graph[i][j] = '.'
        elif graph[i][j] == '*':
            water.append([i, j])

waterBfs()
bfs(x1, y1)