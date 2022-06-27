from collections import deque
def bfs():
    q = deque([1])
    visited[1] = 0
    while q:
        v = q.popleft()
        if v == 100:
            return
        for i in range(1, 7):
            move = v + i
            if 1 <= move <= 100 and visited[move] == 0:
                if move in ladder:
                    move = ladder[move]
                if move in snake:
                    move = snake[move]
                if not visited[move]:
                    visited[move] = visited[v] + 1
                    q.append(move)

n, m = map(int, input().split())
ladder = {}
for _ in range(n):
    tmp = input().split()
    ladder[int(tmp[0])] = int(tmp[1])
snake = {}
for _ in range(m):
    tmp = input().split()
    snake[int(tmp[0])] = int(tmp[1])
visited = [0] * 101
bfs()
print(visited[100])