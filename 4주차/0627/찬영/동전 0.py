# 무지성
import sys
n, target = map(int, input().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
tmp = list(map(lambda x: abs(target-x), coins))
idx = tmp.index(min(tmp))
idx = idx - 1 if coins[idx] > target else idx

check = 0
i = 1
cnt = 0
while check != target:
    cnt += 1
    check += coins[idx]
    if check > target:
        check -= coins[idx]
        cnt -= 1
        idx -= 1
print(cnt)

# 효율성
import sys
n, target = map(int, input().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coins = coins[::-1]

answer = 0
for coin in coins:
    answer += target // coin
    target = target % coin
print(answer)