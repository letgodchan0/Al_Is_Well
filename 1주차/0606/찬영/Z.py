n, r, c = map(int, input().split())
ans = 0

while n != 0:
    n -= 1
    check = 2**n

    if r < check and c < check:
        ans += 0

    elif r < check and c >= check:
        ans += check * check
        c -= check

    elif r >=check  and c < check:
        ans += 2 * check * check
        r -= check
    else:
        ans += 3 * check * check
        r -= check
        c -= check
print(ans)