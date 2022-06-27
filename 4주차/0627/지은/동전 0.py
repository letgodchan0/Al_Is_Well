n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)][::-1]
cnt = 0

for coin in coins:
    tmp = k // coin
    cnt += tmp
    k -= tmp * coin
    if k == 0:
        break
    
print(cnt)
