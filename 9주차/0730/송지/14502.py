from itertools import combinations

def find(arr, virus):
    global n, m, real_ans
    visited = [[0] * m for _ in range(n)]
    ans = 0
    
    for (i, j) in virus:
        visited[i][j] = 1
    
    while virus:
        new_virus = []
        for (i, j) in virus:
            for (di, dj) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and not arr[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    arr[ni][nj] = 2
                    new_virus.append([ni, nj])
        virus = new_virus
        
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                ans += 1
        
    if ans > real_ans:
        print(arr, visited)
        real_ans = ans

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
virus = []
erase = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus.append([i, j])
        elif arr[i][j] == 0:
            erase.append([i, j])
            
real_ans = 0
lst = list(combinations(erase, 3))

for ((ai, aj), (bi, bj), (ci, cj)) in lst:
    arr[ai][aj] = 1
    arr[bi][bj] = 1
    arr[ci][cj] = 1
    
    find(arr, virus)
    arr[ai][aj] = 0
    arr[bi][bj] = 0
    arr[ci][cj] = 0
    
print(real_ans)