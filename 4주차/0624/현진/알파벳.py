# Back_1987
import sys
input = sys.stdin.readline

def bfs(i, j):
    global answer
    # 시간초과를 방지하기 위해 set() 사용
    queue = set([(i, j, board[i][j])])
    while queue:
        i, j, ans = queue.pop()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in ans:
                queue.add((ni, nj, ans + board[ni][nj]))
                answer = max(answer, len(ans) + 1)

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
answer = 1
bfs(0, 0)
print(answer)