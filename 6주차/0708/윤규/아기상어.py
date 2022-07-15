from collections import deque
from copy import deepcopy

n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]
# 위 왼, 오 , 아
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
check = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            si, sj = i, j
            check = 1
            break
    if check == 1:
        break
arr[si][sj] = 0


def shark(x, y, s, e, visited):
    visited = deepcopy(visited)
    q = deque()
    q.append((x,y))
    visited[x][y] = 0
    eat = []
    while q:
        
        i, j = q.popleft()
        
        for di, dj in d:
            ni, nj = i + di, j + dj
            # 범위
            if 0<= ni < n and 0<= nj < n:
                # 물고기 있으면
                if arr[ni][nj] != 0:
                    # 사이즈 더크면
                    if arr[ni][nj] > s:
                        continue
                    # 사이즈가 같고, 방문 x
                    elif arr[ni][nj] == size and visited[ni][nj] == -1:
                        q.append(( ni, nj))
                        visited[ni][nj] = visited[i][j] + 1
                    elif arr[ni][nj] < s:
                        visited[ni][nj] = visited[i][j] + 1
                        eat.append((visited[ni][nj], ni, nj))
                        
                # 물고기 없으면
                else:
                    if visited[ni][nj] == -1:
                        q.append((ni, nj))
                        visited[ni][nj] = visited[i][j] + 1   
    
    # print(eat)
    if eat:
        eat.sort(key=lambda x: (x[0], x[1], x[2]))
        # print(eat)
        dis, ei, ej = eat[0]
        arr[ei][ej] = 0
        e += 1
        if s == e:
            s += 1
            e = 0
        return ei, ej, s, e, dis

    return 0


size = 2
cnt = 0
eat = 0
while True:
    a = shark(si, sj, size, eat, visited)
    
    if not a:
        break
    # print(si, sj, size)
    si, sj, size, eat, c = a
    cnt += c

print(cnt)
for i in range(n):
    print(*arr[i])
    