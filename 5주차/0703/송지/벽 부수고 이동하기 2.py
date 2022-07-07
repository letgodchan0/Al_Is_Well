from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start,K):
    v = [[[-1] * C for _ in range(R)] for _ in range(K+1)]
    queue = deque()
    queue.append([0] + start)
    v[0][start[0]][start[1]] = 0
    
    while queue:
        a, x, y = queue.popleft()
        
        if x == R-1 and y == C-1:
            return v[a][x][y]+1
        
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            
            if 0 <= ax < R and 0 <= ay < C:
                if board[ax][ay] == 1 and a < K and v[a + 1][ax][ay] == -1 :
                    queue.append([a+1,ax,ay])
                    v[a+1][ax][ay] = v[a][x][y] + 1
                elif board[ax][ay] == 0 and v[a][ax][ay] == -1:
                    queue.append([a,ax,ay])
                    v[a][ax][ay] = v[a][x][y] + 1
    return -1

R,C,K = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(R)]

print(bfs([0,0],K))