d, num = map(int, input().split())
x, y = map(int, input().split())

ans = -1
i = j = 0

for n in range(d):
    if str(num)[n] == '1':
        j += 2 ** (d - n - 1)
    elif str(num)[n] == '3':
        i += 2 ** (d - n - 1)
    elif str(num)[n] == '4':
        i += 2 ** (d - n - 1)
        j += 2 ** (d - n - 1)

j += x
i -= y


if 0 <= i < 2 ** d and 0 <= j < 2 ** d:
    ans = ''

    for n in range(d):
        if i >= 2 ** (d - n - 1) and j >= 2 ** (d - n - 1):
            ans += '4'
            i -= 2 ** (d - n - 1)
            j -= 2 ** (d - n - 1)
        elif i >= 2 ** (d - n - 1):
            ans += '3'
            i -= 2 ** (d - n - 1)
        elif j >= 2 ** (d - n - 1):
            ans += '1'
            j -= 2 ** (d - n - 1)
        else:
            ans += '2'

print(ans)
