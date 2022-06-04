def find(color, v):
    global n
    lst = []
    ans = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] in color and not v[i][j]:
                lst.append([i, j])
                while lst:
                    x, y = lst.pop()
                    for (di, dj) in ([0, 1], [1, 0], [0, -1], [-1, 0]):
                        ni = x + di
                        nj = y + dj
                        if 0 <= ni < n and 0 <= nj < n and not v[ni][nj] and arr[ni][nj] in color:
                            v[ni][nj] = 1
                            lst.append([ni, nj])
                ans += 1

    return ans


n = int(input())
arr = [list(input()) for _ in range(n)]
v1 = [[0] * n for _ in range(n)]
v2 = [[0] * n for _ in range(n)]
v3 = [[0] * n for _ in range(n)]
v4 = [[0] * n for _ in range(n)]

r = find(['R'], v1)
g = find(['G'], v2)
b = find(['B'], v3)
rg = find(['R', 'G'], v4)

print(r, g, b, rg)

print(r + g + b, rg + b)
