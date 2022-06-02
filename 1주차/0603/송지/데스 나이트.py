def find(i, j, cnt):
    global ans, gi, gj, n

    lst = [(i, j)]

    while lst:
        new_lst = []
        cnt += 1

        for (i, j) in lst:
            for (di, dj) in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
                ni = i + di
                nj = j + dj

                if ni == gi and nj == gj:
                    ans = cnt
                    return

                if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0:
                    v[ni][nj] = 1
                    new_lst.append([ni, nj])

        lst = new_lst


n = int(input())
i, j, gi, gj = map(int, input().split())

v = [[0] * n for _ in range(n)]
v[i][j] = 1

ans = -1
find(i, j, 0)

print(ans)
