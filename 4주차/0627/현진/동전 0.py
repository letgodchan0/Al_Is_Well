# Back_11047
N, K = map(int, input().split())
coin = []
for _ in range(N):
    money = int(input())
    coin.append(money)

coin.sort(reverse=True)
cnt = 0

for i in coin:
    if i == K:
        break
    elif i < K:
        continue
    cnt += K // i # K // i번 사용했다.
    K = K % 1
print(cnt)