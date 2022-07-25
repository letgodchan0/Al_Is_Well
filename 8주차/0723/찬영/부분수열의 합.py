import sys
from itertools import combinations
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
answer = []
answer.extend(lst)
for i in range(2, len(lst)+1):
    tmp = list(combinations(lst, i))
    for t in tmp:
        answer.append(sum(t))

check = list(set(answer))
check.sort()

result = 0
i = 1
for x in check:
    if x != i:
        result = i
        break
    i += 1
print(result if result else max(list(set(answer)))+1)