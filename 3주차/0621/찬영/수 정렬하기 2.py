import sys
n = int(input())
result = []
for _ in range(n):
    result.append(int(sys.stdin.readline()))
for num in sorted(result):
    print(num)