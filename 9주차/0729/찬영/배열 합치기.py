import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
check = []
check.extend(a)
check.extend(b)
check.sort()
print(*check)

