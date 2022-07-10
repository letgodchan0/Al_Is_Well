def combinations(nums, n):
    result = []
    if n==0:
        return [[]]
    for i in range(len(nums)):
        elem = nums[i]
        for rest in combinations(nums[i+1:],n-1):
            result.append([elem] + rest)
    return result

n, s = map(int, input().split())
nums = list(map(int, input().split()))
combis = []
cnt = 0
for r in range(1, len(nums)+1):
    combis.append(list(combinations(nums, r)))
print(combis)
for combi in combis:
    for c in combi:
        if sum(c)==s:
            cnt += 1
print(cnt)