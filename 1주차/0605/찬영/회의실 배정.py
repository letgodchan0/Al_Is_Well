import sys
n = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

lst.sort(key = lambda x: (x[1],x[0]))
i, j = 0, 0
cnt = 0
for sti, stj in lst:
    if sti >= j:
        i, j = sti, stj
        cnt += 1
print(cnt)