
#########  pypy로는 되고 python으로는 시간초과  #########
r, c = map(int, input().split())
arr = list(input() for _ in range(r))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(i, j, st, cnt):
    global maxV

    maxV = max(maxV, cnt)
    
    for k in range(4):
        di, dj = d[k]
        ni, nj = i + di, j + dj
        if 0<=ni<r and 0<=nj<c and arr[ni][nj] not in st:
            dfs(ni, nj, st+arr[ni][nj], cnt+1)


maxV = 1
dfs(0, 0, f'{arr[0][0]}', 1)
print(maxV)


# st = 'AB'
# a = 'ABCD'
# b = st+a[3]
# if 'AB' in a:
#     print(st+a[3])
#     print(b)

############# python 으로도 빠르게 통과 (구글링) ###################
import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)