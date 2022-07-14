from copy import deepcopy
n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]
# 위 왼, 오 , 아
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
check = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            si, sj = i, j
            check = 1
            break
    if check == 1:
        break
arr[si][sj] = 0


def shark(x, y, s, e, visited):
    visited = deepcopy(visited)
    stack = [(0, x, y, s, e)]
    visited[x][y] = 0
    while stack:
        
        stack.sort(key=lambda x : (x[0], x[1], x[2]))
        
        di, i, j, size, eat = stack.pop(0)
        
        for di, dj in d:
            ni, nj = i + di, j + dj
            # 범위
            if 0<= ni < n and 0<= nj < n:
                # 물고기 있으면
                if arr[ni][nj] != 0:
                    # 사이즈 더크면
                    if arr[ni][nj] > size:
                        continue
                    # 사이즈가 같고, 방문 x
                    elif arr[ni][nj] == size and visited[ni][nj] == -1:
                        stack.append((abs(x-ni) + abs(y-nj), ni, nj, size, eat))
                        visited[ni][nj] = visited[i][j] + 1
                    elif arr[ni][nj] < size:
                        eat += 1
                        if size == eat:
                            size += 1
                            eat = 0
                        arr[ni][nj] = 0
                        
                        return ni, nj, size, eat, visited[i][j] + 1
                # 물고기 없으면
                else:
                    if visited[ni][nj] == -1:
                        stack.append((abs(x-ni) + abs(y-nj), ni, nj, size, eat))
                        visited[ni][nj] = visited[i][j] + 1     
    return 0


size = 2
cnt = 0
eat = 0
while True:
    a = shark(si, sj, size, eat, visited)
    
    if not a:
        break
    print(si, sj, size)
    si, sj, size, eat, c = a
    cnt += c

print(cnt)
for i in range(n):
    print(*arr[i])
    

# for k in range(1, 5):
#     for j in range(-1*k, k+1):
#         t = abs(k)-abs(j)
#         if t != 0:
#             print((j, (abs(k)-abs(j))*-1))
#             print((j, (abs(k)-abs(j))))
#         else: print(j, 0)
    