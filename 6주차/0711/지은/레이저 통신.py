import sys
input = sys.stdin.readline

w, h = map(int, input().split())
mat = []
for i in range(h):
    mat.append(input())

mirror = [[] for _ in range(h)]
C = []
for i in range(h):
    for j in range(w):
        if mat[i][j] == 'C':
            C.append([i, j])
        if mat[i][j] != '*':
            mirror[i].append(-1)
        else:
            mirror[i].append(mat[i][j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start_y, start_x):
    q = []
    q.append([start_y, start_x])
    mirror[start_y][start_x] = 0
    while q:
        y, x,  = q.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            while 0 <= ny < h and 0 <= nx < w:
                if mirror[ny][nx] == '*':
                    break
                if mirror[ny][nx] == -1:
                    mirror[ny][nx] = mirror[y][x] + 1
                    q.append([ny, nx])
                nx += dx[i]
                ny += dy[i]

bfs(C[0][0], C[0][1])
print(mirror[C[1][0]][C[1][1]] - 1)