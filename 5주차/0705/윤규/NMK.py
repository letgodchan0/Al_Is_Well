n, m, k = map(int, input().split())

if n < m+k-1 or n > m*k:
    print(-1)
else:
    l = list(range(k, 0, -1))
    n -= k
    m -= 1
    while m:
        l.extend(range(k+n//m , k, -1))
        k += n//m
        n -= n//m
        m -= 1
    print(*l)