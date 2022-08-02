import sys
sys.setrecursionlimit(100000000)

def find(i, j, ans, cnt):
    global arr, n, m, answer, v
    
    if ans >= answer:
        return
    
    if i == n - 1 and j == m - 1:
        if ans < answer:
            answer = ans
        return
    
    for (di, dj) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0:
            if arr[ni][nj] == 1 and cnt:
                v[ni][nj] = 1
                find(ni, nj, ans + 1, 0)
                v[ni][nj] = 0
            elif arr[ni][nj] == 0:
                v[ni][nj] = 1
                find(ni, nj, ans + 1, cnt)
                v[ni][nj] = 0
    

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

answer = 1000000
v[0][0] = 1
find(0, 0, 1, 1)

if answer == 1000000:
    print(-1)
else:
    print(answer)