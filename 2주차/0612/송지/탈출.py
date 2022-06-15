r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]
ans = 'KAKTUS'
cnt = 0

water = []
goseum = []

for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            water.append((i, j))
        elif arr[i][j] == 'S':
            goseum.append((i, j))

while goseum and ans == 'KAKTUS':
    cnt += 1
    new_water = []
    new_goseum = []

    for (wi, wj) in water:
        for (di, dj) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = wi + di
            nj = wj + dj
            if 0 <= ni < r and 0 <= nj < c and (arr[ni][nj] == '.' or arr[ni][nj] == 'S'):
                arr[ni][nj] = '*'
                new_water.append([ni, nj])

    for (gi, gj) in goseum:
        for (di, dj) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = gi + di
            nj = gj + dj
            if 0 <= ni < r and 0 <= nj < c and (arr[ni][nj] == '.' or arr[ni][nj] == 'D'):
                if arr[ni][nj] == 'D':
                    ans = cnt
                arr[ni][nj] = 'S'
                new_goseum.append([ni, nj])

    water = new_water
    goseum = new_goseum

print(ans)
