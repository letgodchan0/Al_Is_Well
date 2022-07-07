from itertools import combinations

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = 2 ** 99

arr = list(combinations(list(range(n)), 2))

for (a, b) in arr:
    tmp = (lst[a][0] - lst[b][0]) ** 2 + (lst[a][1] - lst[b][1]) ** 2
    if tmp < ans:
        ans = tmp
        
print(ans)