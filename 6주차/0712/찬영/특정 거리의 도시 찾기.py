import sys, heapq

def dijkstra():
    heap = []
    heapq.heappush(heap, [0, x])

    d[x] = 0
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)

        for v, w in adj[cur_node]:
            tmp = cur_cost + w
            if d[v] > tmp:
                d[v] = tmp
                heapq.heappush(heap, (tmp, v))


n, m, k, x = map(int, input().split())
INF = int(1e9)
adj = [[] for _ in range(n+1)]
d = [INF] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append((b, 1))
dijkstra()

if d.count(k):
    for i in range(1, n+1):
        if d[i] == k:
            print(i)
else:
    print(-1)
