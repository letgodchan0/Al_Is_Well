n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

ans = 0
tmp = 0

for num in lst:
    if num > 0:
        break
    elif not tmp:
        tmp += num
    elif tmp * num > tmp:
        ans += tmp * num
        tmp = 0
    else:
        ans += tmp
        tmp = num

if tmp:
    ans += tmp
    tmp = 0

for num in lst[::-1]:
    if num <= 0:
        break
    elif not tmp:
        tmp += num
    elif tmp * num > tmp:
        ans += tmp * num
        tmp = 0
    else:
        ans += tmp
        tmp = num

ans += tmp

print(ans)
