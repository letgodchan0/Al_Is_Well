import sys
input = sys.stdin.readline
n = int(input())

numlst = [0] * 10001
for i in range(n):
    numlst[int(input())] += 1


for i in range(len(numlst)):
    k = numlst[i]
    if k > 0:
        for _ in range(k):
            print(i)

