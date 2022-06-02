def find(i1, j1, i2, j2, c):
    global ans, n, m

    if c > 10 or c >= ans:
        return

    if arr[i1][j1] == 'x' and arr[i2][j2] != 'x':
        ans = c
        return
    elif arr[i1][j1] != 'x' and arr[i2][j2] == 'x':
        ans = c
        return
    else:
        for (di, dj) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni1 = i1 + di
            nj1 = j1 + dj
            ni2 = i2 + di
            nj2 = j2 + dj

            # print(i1, j1, i2, j2)
            # print(ni1, nj1, ni2, nj2)

            if arr[ni1][nj1] == 'x' and arr[ni2][nj2] == 'x':
                pass
            elif arr[ni1][nj1] == '#' and arr[ni2][nj2] == '#':
                pass
            elif arr[ni1][nj1] == '#':
                find(i1, j1, ni2, nj2, c + 1)
            elif arr[ni2][nj2] == '#':
                find(ni1, nj1, i2, j2, c + 1)
            else:
                find(ni1, nj1, ni2, nj2, c + 1)


n, m = map(int, input().split())
arr = [['x'] * (m + 2)] + [['x'] + list(input()) + ['x']
                           for _ in range(n)] + [['x'] * (m + 2)]

c1 = c2 = ''

for i in range(n + 2):
    for j in range(m + 2):
        if arr[i][j] == 'o' and c1:
            c2 = [i, j]
            break
        elif arr[i][j] == 'o':
            c1 = [i, j]

ans = 11
find(c1[0], c1[1], c2[0], c2[1], 0)

if ans == 11:
    print(-1)
else:
    print(ans)
