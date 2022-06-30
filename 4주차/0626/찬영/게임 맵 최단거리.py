from collections import deque

def bfs(n, m, maps):
    q = deque([])
    q.append((0,0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m - 1:
            return visited[x][y]

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return -1
def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = bfs(n, m, maps)
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))