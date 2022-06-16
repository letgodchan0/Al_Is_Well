import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        a = 0

        if arr[i][j]:
            lst = [(i, j)]
            v = [[0] * m for _ in range(n)]
            v[i][j] = 1
            a += 1

            while lst:
                new_lst = []
                for (pi, pj) in lst:
                    for (di, dj) in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                        ni = pi + di
                        nj = pj + dj
                        if 0 <= ni < n and 0 <= nj < m and not arr[ni][nj] and not v[ni][nj]:
                            new_lst.append([ni, nj])
                            v[ni][nj] = 1
                            a += 1
                lst = new_lst

        print(a % 10, end='')

    print('')
