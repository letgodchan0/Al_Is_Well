# 머야 sys 없을때는 시간초과, sys import 하면 정답가능 => ???
import sys
input = sys.stdin.readline

n = int(input())
xylst = []
for i in range(n):
    xy = tuple(map(int, input().split(' ')))
    xylst.append(xy)


xylst.sort(key=lambda x: (x[1], x[0]))

for x, y in xylst:
    print(x, y)
