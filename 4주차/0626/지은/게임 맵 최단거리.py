from collections import deque

def bfs(x, y, maps):
    me = deque()
    me.append((x, y))
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    n, m = len(maps), len(maps[0])
    while me:
        i, j = me.popleft()
        for di, dj in move:
            ni = i + di
            nj = j + dj
            if ni in range(n) and nj in range(m) and (maps[ni][nj]==1 or maps[ni][nj]==-1):
                maps[ni][nj] = maps[i][j] + 1
                me.append((ni,nj))
    return maps[n-1][m-1] 

def solution(maps):
    maps[-1][-1] = -1 #상대팀 진영의 값을 -1로 둔다(1로 두면 결과를 판단할 때 거리가 1인지 못가서 1인지 모르므로)
    return bfs(0, 0, maps) 
    
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))