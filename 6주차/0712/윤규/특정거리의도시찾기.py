# 메모리초과
n, m, k, x = map(int, input().split(' '))
roads = dict()
visited = [999999999999999] * (n + 1)
xs = [x]
for _ in range(m):
    start, end = map(int, input().split(' '))
    if roads.get(start):
        roads[start].append(end)
    else:
        roads[start] = [end]

visited[x] = 0
for i in range(1, k+1):
    new_xs = []
    for x in xs:
        if roads.get(x):
            for start in roads[x]:
                if visited[start] > i:
                    visited[start] = i
                new_xs.append(start)
       
    
    xs = new_xs
plst = []
for i in range(len(visited)):
    if visited[i] == k:
        plst.append(i)

if not plst:
    print(-1)
else:
    
    for p in plst:
        print(p)



# 구글링
from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)