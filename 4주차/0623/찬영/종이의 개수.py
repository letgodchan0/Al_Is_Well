n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
number = {-1 : 0, 0 : 0, 1 : 0}

def check(x, y, n, num):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                return False
    return True

def dac(x, y, n, num):
    global cnt
    if check(x, y, n, num):
        number[num] += 1
    else:
        n = n // 3
        dac(x, y, n, arr[x][y])
        dac(x+n, y, n, arr[x+n][y])
        dac(x+(2*n), y, n, arr[x+(2*n)][y])
        dac(x, y+n, n, arr[x][y+n])
        dac(x, y+(2*n), n, arr[x][y+(2*n)])
        dac(x+n, y+n, n, arr[x+n][y+n])
        dac(x+n, y+(2*n), n, arr[x+n][y+(2*n)])
        dac(x+(2*n), y+n, n, arr[x+(2*n)][y+n])
        dac(x+(2*n), y+(2*n), n, arr[x+(2*n)][y+(2*n)])

dac(0, 0, n, arr[0][0])
print(number[-1])
print(number[0])
print(number[1])