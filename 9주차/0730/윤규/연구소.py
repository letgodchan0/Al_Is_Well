from copy import deepcopy
from itertools import combinations
n, m =  map(int, input().split(' '))
arr2 = [list(map(int, input().split(' '))) for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
maxV = 0


blank = []
for i in range(n):
    for j in range(m):
        if arr2[i][j] == 0:
            blank.append([i, j])

def virus(i, j):
    q = [(i, j)]
    while q:
        x, y = q.pop(0)
        for di, dj in d:
            ni, nj = x + di, y + dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 0:
                arr[ni][nj] = 2
                q.append((ni,nj))
    
                
for dots in list(combinations(blank, 3)):
    arr = deepcopy(arr2)
    for i in range(3):
        arr[dots[i][0]][dots[i][1]] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                virus(i, j)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    if cnt > maxV:
        maxV = cnt


print(maxV)