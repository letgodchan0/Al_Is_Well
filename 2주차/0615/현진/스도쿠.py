import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
check = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_checking(i, j):
    checking = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if sudoku[i][k] in checking:
            checking.remove(sudoku[i][k])
        if sudoku[k][j] in checking:
            checking.remove(sudoku[k][j])
    i //= 3
    j //= 3
    for p in range(i * 3, (i + 1) * 3):
        for q in range(j * 3, (j + 1) * 3):
            if sudoku[p][q] in checking:
                checking.remove(sudoku[p][q])
    return checking

flag = False
def dfs(x):
    global flag

    if flag:
        return
    
    if x == len(check):
        for row in sudoku:
            print(*row)
        flag = True
        return
    else:
        (i, j) = check[x]
        checking = is_checking(i, j)

        for num in checking:
            sudoku[i][j] = num
            dfs(x + 1)
            sudoku[i][j] = 0
dfs(0)