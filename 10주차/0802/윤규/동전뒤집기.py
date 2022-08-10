n = int(input())
coin = [list(input()) for _ in range(n)]
ans = n * n + 1

for bit in range(1 << n):
    tmp = [coin[i][:] for i in range(n)]
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                if tmp[i][j] == 'H':
                    tmp[i][j] = 'T'
                else:
                    tmp[i][j] = 'H'

    tot = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if tmp[j][i] == 'T':
                cnt += 1
        tot += min(cnt, n-cnt)
    ans = min(ans, tot)

print(ans)