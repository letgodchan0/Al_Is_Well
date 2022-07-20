n, m = map(int, input().split(' '))
arr1 = [list(map(int, input())) for _ in range(n)]
arr2 = [list(map(int, input())) for _ in range(n)]


def change(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if arr1[x][y] == 1:
                arr1[x][y] = 0
            else:
                arr1[x][y] = 1

cnt = 0
if (n<3 or m<3) and arr1 != arr2:
    cnt = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if arr1[i][j] != arr2[i][j]:
                change(i,j)
                cnt += 1
    if arr1 != arr2:
        cnt = -1
print(cnt)