# from collections import deque
# def solution(maps):
#     answer = -1
#     di = (1, 0, -1, 0)
#     dj = (0, -1, 0, 1)
#     n = len(maps)
#     m = len(maps[0])
#     visited = [[0] * m for _ in range(n)]
#     check = 0
#     stack = deque()
#     stack.append((0,0,1))
    
#     while stack:
#         i, j, cnt = stack.popleft()
#         visited[i][j] = 1
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0<=ni< n and 0<=nj<m and maps[ni][nj] == 1 and visited[ni][nj] == 0:
#                 stack.append((ni, nj, cnt+1))
#                 if ni == n-1 and nj == m-1:
#                     answer = cnt + 1
#                     check = 1
#                     break
                
                
#         if check == 1:
            
#             break


#     return answer




## 효율성도 통과 머가 다른거지;;  한개 차이가 이렇게 큰가;;
from collections import deque
def solution(maps):
    
    di = (1, 0, -1, 0)
    dj = (0, -1, 0, 1)
    n = len(maps)
    m = len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1
    check = 0
    stack = deque()
    stack.append((0,0))
    
    while stack:
        i, j= stack.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni< n and 0<=nj<m and maps[ni][nj] == 1 and visited[ni][nj] == -1:
                stack.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if ni == n-1 and nj == m-1:
                    check = 1
                    break
                
                
        if check == 1:
            
            break

    answer = visited[n-1][m-1]
    return answer




print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))