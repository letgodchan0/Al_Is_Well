def dfs(x, total):
    global cnt
    if x >= N:
        return 
    total += arr[x]
    if total == S:
        cnt += 1
    dfs(x + 1, total - arr[x])
    dfs(x + 1, total)
    
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)