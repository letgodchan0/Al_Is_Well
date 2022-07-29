n, k = map(int, input().split(' '))

cnt = 0

a = []
check = 0
cntb = n - 1
cntmax = 0
while cnt != k:
    cnt -= len(a)
    cntb -= 1
    for i in range(n-2, len(a) - 1, -1):
        if i == len(a):
            a.append(i)
        cnt += 1
        if cnt == k:
            a.append(i)
            break
    if cnt == k:
        break
    if cntb < 0:
        check = 1
        break

ans = ''
if check == 1:
    print(-1)
else:
    for i in range(n):
        if i in a:
            ans += 'A'
        else:
            ans += 'B'

    print(ans)


