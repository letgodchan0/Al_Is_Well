n, k = map(int, input().split(' '))
money = []
for i in range(n):
    money.append(int(input()))

cnt = 0
for i in range(n-1, -1, -1):
    if money[i] > k:
        continue
    cnt += k // money[i]
    k = k % money[i]
    if k == 0:
        break
print(cnt)