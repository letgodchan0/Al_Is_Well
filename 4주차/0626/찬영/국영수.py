import sys
n = int(input())
lst = []
for _ in range(n):
    name, korean, english, math = sys.stdin.readline().split()
    lst.append([name, int(korean), int(english), int(math)])
lst.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for l in lst:
    print(l[0])