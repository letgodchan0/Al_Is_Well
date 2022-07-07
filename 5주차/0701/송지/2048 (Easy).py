from copy import deepcopy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def up(graph):
    for j in range(n):
        p = 0

        for i in range(1, n):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0

                if graph[p][j] == 0:
                    graph[p][j] = temp

                elif graph[p][j] == temp:
                    graph[p][j] *= 2
                    p += 1

                else:
                    p += 1
                    graph[p][j] = temp

    return graph

def down(graph):
    for j in range(n):
        p = n - 1

        for i in range(n - 2, -1, -1):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0

                if graph[p][j] == 0:
                    graph[p][j] = temp
                elif graph[p][j] == temp:
                    graph[p][j] *= 2
                    p -= 1
                else:
                    p -= 1
                    graph[p][j] = temp

    return graph

def left(graph):
    for i in range(n):
        p = 0

        for j in range(1, n):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0

                if graph[i][p] == 0:
                    graph[i][p] = temp
                elif graph[i][p] == temp:
                    graph[i][p] *= 2
                    p += 1
                else:
                    p += 1
                    graph[i][p] = temp

    return graph

def right(graph):
    for i in range(n):
        p = n - 1

        for j in range(n - 2, -1, -1):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0

                if graph[i][p] == 0:
                    graph[i][p] = temp
                elif graph[i][p] == temp:
                    graph[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    graph[i][p] = temp

    return graph

def dfs(graph, cnt):
    global ans

    if cnt == 5:
        ans = max(ans, max(map(max, graph)))
        return

    dfs(up(deepcopy(graph)), cnt + 1)
    dfs(down(deepcopy(graph)), cnt + 1)
    dfs(left(deepcopy(graph)), cnt + 1)
    dfs(right(deepcopy(graph)), cnt + 1)

dfs(graph, 0)
print(ans)