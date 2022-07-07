import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0] * m for i in range(n + 1)]
b = [[0] * m for i in range(n + 1)]

for i in range(1, n+1):
    num = int(input())
    for j in range(1, min(m, (i+1)//2)+1):
        b[i][j] = max(a[i - 1][j], b[i - 1][j])
        a[i][j] = max(a[i - 1][j], b[i - 1][j - 1]) + num
print(max(a[n][m], b[n][m]))