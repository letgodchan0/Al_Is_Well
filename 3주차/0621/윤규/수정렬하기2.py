import sys
input = sys.stdin.readline
n = int(input())

numlst = []
for _ in range(n):
    numlst.append(int(input()))
numlst.sort()
for num in numlst:
    print(num)