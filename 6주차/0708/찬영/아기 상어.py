from collections import deque

def bfs(sti, stj, weight, cnt):
    global res
    q = deque([])
    i, j = sti, stj
    q.append((i, j))
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1
    distance = 0
    while q:
        distance += 1
        check = deque([])
        eat = []
        for x, y in q:
            for dx, dy in [(-1,0), (0,-1), (1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and 0 < arr[nx][ny] < weight and not visited[nx][ny]:
                    eat.append((nx, ny))
                elif 0 <= nx < n and 0 <= ny < n and (arr[nx][ny] == 0 or arr[nx][ny] == weight) and not visited[nx][ny]:
                    check.append((nx,ny))
                    visited[nx][ny] = 1

        if eat:
            eat.sort()
            i, j = eat[0]
            cnt += 1
            arr[i][j] = arr[sti][stj] = 0

            res += distance
            if cnt == weight:
                weight += 1
                cnt = 0
            return bfs(i, j, weight, cnt)

        q = check

    return


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0     # 시간
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sti, stj = i, j
            break

bfs(sti, stj, 2, 0)
print(res)