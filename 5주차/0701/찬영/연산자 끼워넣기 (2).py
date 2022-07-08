def dfs(idx, check):
    global max_val, min_val

    if idx == n:
        max_val = max(max_val, check)
        min_val = min(min_val, check)
        return

    if tmp[0] > 0:
        tmp[0] -= 1
        dfs(idx + 1, check + lst[idx])
        tmp[0] += 1

    if tmp[1] > 0:
        tmp[1] -= 1
        dfs(idx + 1, check - lst[idx])
        tmp[1] += 1

    if tmp[2] > 0:
        tmp[2] -= 1
        dfs(idx + 1, check * lst[idx])
        tmp[2] += 1

    if tmp[3] > 0:
        tmp[3] -= 1
        dfs(idx + 1, int(check / lst[idx]))
        tmp[3] += 1

n = int(input())
lst = list(map(int, input().split()))
tmp = list(map(int, input().split()))
max_val = -1000000000
min_val = 1000000000

dfs(1, lst[0])
print(max_val)
print(min_val)