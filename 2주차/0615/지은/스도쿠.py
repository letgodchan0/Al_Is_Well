def row_check(x, a):
    for i in range(9):
        if a == su[x][i]:
            return False
    return True

def col_check(y, a):
    for i in range(9):
        if a == su[i][y]:
            return False
    return True

def box_check(x, y, a):
    x_start = x//3*3
    y_start = y//3*3
    for i in range(3):
        for j in range(3):
            if a == su[x_start+i][y_start+j]:
                return False
    return True

def dfs(n):
    if n == len(blank_xy):
        for i in range(9):
            print(*su[i])
        exit()
        #return 시 탐색을 이어서 하게되며 모든 답을 찾아내고 모두 출력할 때까지 프로그램이 끝나지 않음
    for num in range(1,10):
        x, y = blank_xy[n][0], blank_xy[n][1]
        if row_check(x, num) and col_check(y, num) and box_check(x, y, num):
            su[x][y] = num
            dfs(n+1)
            su[x][y] = 0

su = [list(map(int, input().split())) for _ in range(9)]

blank_xy = []
for i in range(9):
    for j in range(9):
        if su[i][j]==0:
            blank_xy.append((i,j))

dfs(0)