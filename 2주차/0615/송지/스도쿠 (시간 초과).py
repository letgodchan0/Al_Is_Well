import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
garo = [0] * 9
sero = [0] * 9
square = [0] * 9

sum_ga = [0] * 9
sum_se = [0] * 9
sum_sq = [0] * 9

for i in range(9):
    for j in range(9):
        sum_ga[i] += arr[i][j]
        sum_se[j] += arr[i][j]
        sum_sq[(i // 3) * 3 + j // 3] += arr[i][j]
        if not arr[i][j]:
            garo[i] += 1
            sero[j] += 1
            square[(i // 3) * 3 + j // 3] += 1


while garo != [0] * 9:

    for i in range(9):
        for j in range(9):

            if arr[i][j] == 0:

                if garo[i] == 1:
                    arr[i][j] = 45 - sum_ga[i]
                    garo[i] -= 1
                    sero[j] -= 1
                    square[(i // 3) * 3 + j // 3] -= 1

                    sum_ga[i] += arr[i][j]
                    sum_se[j] += arr[i][j]
                    sum_sq[(i // 3) * 3 + j // 3] += arr[i][j]

                elif sero[j] == 1:
                    arr[i][j] = 45 - sum_se[j]
                    garo[i] -= 1
                    sero[j] -= 1
                    square[(i // 3) * 3 + j // 3] -= 1

                    sum_ga[i] += arr[i][j]
                    sum_se[j] += arr[i][j]
                    sum_sq[(i // 3) * 3 + j // 3] += arr[i][j]

                elif square[(i // 3) * 3 + j // 3] == 1:
                    arr[i][j] = 45 - sum_sq[(i // 3) * 3 + j // 3]
                    garo[i] -= 1
                    sero[j] -= 1
                    square[(i // 3) * 3 + j // 3] -= 1

                    sum_ga[i] += arr[i][j]
                    sum_se[j] += arr[i][j]
                    sum_sq[(i // 3) * 3 + j // 3] += arr[i][j]


for i in range(9):
    for j in range(9):
        print(arr[i][j], end=' ')
    print('')
