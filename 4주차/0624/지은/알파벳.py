import sys

def dfs(i, j, cnt):
    global ans
    ans = max(ans, cnt)
    for di, dj in move:
        ni = i + di
        nj = j + dj
        if 0<=ni<r and 0<=nj<c and arr[ni][nj] not in visited:
            visited.add(arr[ni][nj])
            dfs(ni, nj, cnt +1)
            visited.remove(arr[ni][nj])

r, c = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(r)]
move = [(-1,0), (0,-1), (1, 0), (0, 1)]
visited = set(arr[0][0])
ans = 0
dfs(0, 0, 1)
print(ans)