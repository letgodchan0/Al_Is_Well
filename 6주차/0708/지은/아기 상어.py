from collections import deque

def eat(x, y, size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    position = deque()
    position.append((x,y))
    visited[x][y] = 1
    tmp = []
    while position:
        x, y = position.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if arr[nx][ny] <= size:
                    position.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    if arr[nx][ny]<size and arr[nx][ny] != 0:
                        tmp.append((nx,ny,distance[nx][ny])) 
    return sorted(tmp,key=lambda x:(-x[2],-x[0],-x[1]))
    #거리가 가까운 물고기들이 많다면 가장 위, 가장 왼쪽의 물고기를 먹는다
    
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    if 9 in arr[-1]:
        x, y = i, arr[-1].index(9)
size = 2
cnt, result = 0, 0
move = [(1,0),(0,1),(-1,0),(0,-1)]

while True:
    shark = eat(x,y,size)
    if len(shark)==0:           #먹을 수 있는 물고기가 없을 때
        break
    nx,ny,time = shark.pop()    #먹을 수 있는 물고기가 많을 때

    result += time              #시간을 더해준다
    arr[x][y],arr[nx][ny] = 0, 0    #상어의 자리, 먹이가 있던 자리 0으로
    x, y = nx, ny   #상어의 자리를 옮겨준다
    cnt += 1        #상어가 먹은 수 
    if cnt == size: #size와 같다면 상어의 size 키워주기 
        size += 1
        cnt = 0

print(result)