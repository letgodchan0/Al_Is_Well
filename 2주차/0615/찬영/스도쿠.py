import sys
sys.setrecursionlimit(10**9)

def get_possible(i, j):
    num = set('123456789')
    row = set(table[i])
    col = set([table[t][j] for t in range(9)])
    box = set([table[p][q] for p in range(3*(i//3), 3*(i//3) + 3) for q in range(3*(j//3), 3*(j//3) + 3)])

    num = num.difference(row)
    num = num.difference(col)
    num = num.difference(box)

    return num

def solve(idx):
    if idx == len_zero:
        return True
    
    i, j = zero[idx]
    vset = get_possible(i, j)
    for v in vset:
        table[i][j] = v
        if solve(idx+1):
            return True
        else:
            table[i][j] = '0'
    return False

table = [list(sys.stdin.readline().split()) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if table[i][j] == '0':
            zero.append((i, j))

len_zero = len(zero)
if len_zero > 0:
    solve(0)

for t in table:
    print(' '.join(t))