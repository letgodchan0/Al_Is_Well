from itertools import combinations
N, S = map(int, input().split()) # N개의 정수의 합이 S
arr = list(map(int, input().split()))
cnt = 0

for r in range(1, len(arr)+1):
    part = list(combinations(arr, r))
    for l in part:
        s = 0
        for m in l:
            s += m
        if s == S:
            cnt += 1
print(cnt)