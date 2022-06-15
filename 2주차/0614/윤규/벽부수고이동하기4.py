from collections import deque
n, m = map(int, input().split(' '))
arr = [list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
pos = [[1] * m for _ in range(n)]
d = [(1,0), (-1,0), (0,1), (0,-1)]
# 0인 곳에서 갈 수 있는 갯수 구하기
def search(i, j):
    q = deque([])
    q.append((i,j))
    one = [(i,j)]
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni,nj))
                one.append((ni,nj))
    # 갈수 있는 곳 모든 리스트 담기
    for i, j in one:
        pos[i][j] = one
    
    
# pos 를 1과 갈수 있는 리스트로 다 바꿈 
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            search(i,j)

# arr가 1인 곳에서 갈수 있는 곳 개수 구하기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt = 1
            lst = []
            for di, dj in d:
                ni, nj = i + di, j + dj
                # 범위 안에 있고, 1(벽)이 아니고 
                if 0<=ni<n and 0<=nj<m and pos[ni][nj] != 1 and pos[ni][nj] not in lst:
                    cnt += len(pos[ni][nj])
                    lst.append(pos[ni][nj])
            arr[i][j] = cnt % 10


for i in range(n):
    for j in range(m):
        print(arr[i][j], end='')
    print()