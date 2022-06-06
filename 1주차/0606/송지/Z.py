def find(n, i, j):

    if n == 0:
        return

    if i < 2 ** n / 2 and j < 2 ** n / 2:  # 좌상
        lst.append(0)
        find(n - 1, i, j)
    elif i < 2 ** n / 2:  # 우상
        lst.append(1)
        find(n - 1, i, j - 2 ** (n - 1))
    elif j < 2 ** n / 2:  # 좌하
        lst.append(2)
        find(n - 1, i - 2 ** (n - 1), j)
    else:  # 우하
        lst.append(3)
        find(n - 1, i - 2 ** (n - 1), j - 2 ** (n - 1))


n, r, c = map(int, input().split())
lst = []
ans = 0

find(n, r, c)

for i in range(n):
    ans += 4 ** (n - i - 1) * lst[i]

print(ans)
