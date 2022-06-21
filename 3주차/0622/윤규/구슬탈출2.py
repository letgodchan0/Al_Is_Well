n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
d = [(1,0), (-1,0), (0,1), (0,-1)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'B':
            bi, bj = i, j
        if arr[i][j] == 'R':
            ri, rj = i, j
        if arr[i][j] == 'O':
            hi, hj = i, j


def end(i):
    di = d[i]
    while 


def search(i, s):
    if i > 10:
        return -1
    
    for j in range(4):
        if j != s:
            end(j)
            
