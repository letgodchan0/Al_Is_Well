from itertools import combinations

n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

for i in range(1, n + 1):
    for s_lst in list(combinations(lst, i)):
        if sum(s_lst) == s:
            ans += 1
            
print(ans)