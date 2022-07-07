n, m, k = map(int, input().split())

k -= n % 2
n -= n % 2
t = 0

n = n // 2
if n > m:
    k -= (n - m) * 2
    n = m
elif n < m:
    k -= (m - n)

if k > 0:
    n -= k // 3
    k -= (k // 3) * 3

    if k % 3:
        n -= 1
    print(n)
else:
    print(min(n, m))