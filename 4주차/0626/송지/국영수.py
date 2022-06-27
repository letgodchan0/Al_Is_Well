import sys
input = sys.stdin.readline

n = int(input())
lst = [list(input().split()) for _ in range(n)]
lst = sorted(lst, key=lambda x: (
    100 - int(x[1]), int(x[2]), 100 - int(x[3]), x[0]))

for i in range(n):
    print(lst[i][0])
