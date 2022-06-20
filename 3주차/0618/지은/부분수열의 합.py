from itertools import combinations
n, s = map(int, input().split())
nums = list(map(int, input().split()))
combis = []
cnt = 0
for r in range(1, len(nums)+1):
    combis.append(list(combinations(nums, r)))
for combi in combis:
    for c in combi:
        if sum(c)==s:
            cnt += 1
print(cnt)

#dfs로 풀어보기
def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += nums[idx]
    if sum == s:
        cnt+=1
    dfs(idx+1, sum-nums[idx])
    dfs(idx+1, sum)

n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
dfs(0,0)
print(cnt)