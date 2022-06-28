from collections import deque

def bfs(now):
    me = deque([now])
    visited[now] = 1
    while me:
        now = me.popleft()
        for dice in [1,2,3,4,5,6]:
            new = now + dice    #이동 전
            if new in range(1,101):
                if new in ladders:
                    new = ladders[new]
                elif new in snakes:
                    new = snakes[new]
                if visited[new]==0:
                    me.append(new)
                    visited[new] = visited[now] + 1            
            if new==100:
                print(visited)
                return visited[100]-1

n, m = map(int, input().split())

ladders = {}
for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

snakes = {}
for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v

visited = [0] * (101)   #1~100

print(bfs(1))