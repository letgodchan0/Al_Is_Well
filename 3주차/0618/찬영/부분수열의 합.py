import sys
from itertools import combinations
n, s = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
lst = []
for i in range(1, n+1):
    for num in list(map(list, combinations(numbers, i))):
        if sum(num) == s:
            lst.append(num)

print(len(lst))
