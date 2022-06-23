from collections import deque

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = [] # 방문여부를 판단하기 위한 리스트
    visited.append((rx, ry, bx, by))
    cnt = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if cnt > 10: # 움직인 횟수가 10회 초과면 -1 출력
                print(-1)
                return
            if arr[rx][ry] == 'O': # 현재 빨간 구슬의 위치가 구멍이라면 cnt출력
                print(cnt)
                return 
            for i in range(4):  # 4방향 탐색
                nrx, nry = rx, ry
                while True:                  # #일 때까지 혹은 구멍일 때까지 움직임
                    nrx += move[i][0]
                    nry += move[i][1]
                    if arr[nrx][nry] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nrx -= move[i][0]
                        nry -= move[i][1]
                        break
                    if arr[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True:                  # #일 때까지 혹은 구멍일 때까지 움직임
                    nbx += move[i][0]
                    nby += move[i][1]
                    if arr[nbx][nby] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nbx -= move[i][0]
                        nby -= move[i][1]
                        break
                    if arr[nbx][nby] == 'O':
                        break
                if arr[nbx][nby] == 'O':     # 파란구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                    continue
                if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= move[i][0]
                        nry -= move[i][1]
                    else:
                        nbx -= move[i][0]
                        nby -= move[i][1]
                if (nrx, nry, nbx, nby) not in visited: # 방문해본적이 없는 위치라면 새로 큐에 추가 후 방문 처리
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
    print(-1) # 10회가 초과하지 않았지만 10회 내에도 구멍에 들어가지 못하는 경우

n, m = map(int, input().split())    #세로가로
arr = [] 
move = [(1,0),(0,1),(-1,0),(0,-1)]  
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    arr.append(list(input()))
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j]=='B':
            bx, by = i, j

bfs(rx, ry, bx, by)            