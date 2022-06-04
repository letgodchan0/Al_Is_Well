def bfs(i, j):
    q.append((i,j))
    visited[i][j] = 1
    while(q):
        i, j = q.popleft()
        for di, dj in move:
            ni = i + di
            nj = j + dj
            if ni in range(n) and nj in range(n) and visited[ni][nj]==0 and pic[i][j]==pic[ni][nj]:
                visited[ni][nj]=1
                q.append((ni,nj))

from collections import deque
n = int(input())   #n개의 줄 
pic = [list(input()) for _ in range(n)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque()

#적록색약이 아닌 사람
visited = [[0]*n for _ in range(n)]
groups = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i, j)
            groups+=1

#적록색약인 사람
for i in range(n):  #초록색을 빨간색으로 바꿈
    for j in range(n):
        if pic[i][j]=='G':
            pic[i][j]='R'

visited = [[0]*n for _ in range(n)]
groups_gr = 0   
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i, j)
            groups_gr+=1

print(groups, groups_gr)