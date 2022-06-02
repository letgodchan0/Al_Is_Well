from collections import deque
def bfs(x, y):
    q = deque([])
    q.append((x, y))
    visited = [[0] * n for _ in range(n)]
    while q:
        x, y = q.popleft()
        if x == r2 and y == c2:
            return visited[x][y]
        for dx, dy in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return -1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

print(bfs(r1, c1))