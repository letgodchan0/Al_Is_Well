
from collections import deque

di = [0, 1, 0, -1]  
dj = [1, 0, -1, 0]
n, m, k = map(int, input().split(' '))
arr = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]


q = deque()
q.append([0,0,0])
visited[0][0][0] = 1
check = 0
while q:
    # print(q)
    # print(visited)
    i, j, cnt = q.popleft()
    if i == n-1 and j == m-1:
        print(visited[i][j][cnt])
        check = 1
        break
    for l in range(4):
        ni, nj = i + di[l], j + dj[l]
        if 0<= ni < n and 0<= nj <m:
            if not visited[ni][nj][cnt]:
                # print(arr[ni][nj], cnt, k)
                if arr[ni][nj] and cnt < k:
                    # print('!')
                    visited[ni][nj][cnt+1] = visited[i][j][cnt] + 1
                    q.append([ni, nj, cnt+1])

                elif not arr[ni][nj]:
                    visited[ni][nj][cnt] = visited[i][j][cnt] + 1
                    q.append([ni, nj, cnt])
    # print(q)

if check == 0:
    print(-1)