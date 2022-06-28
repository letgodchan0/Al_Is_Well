from collections import deque
def solution(maps):
    answer = -1
    di = (1, 0, -1, 0)
    dj = (0, -1, 0, 1)
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    check = 0
    # cnt = [[n*m+1] * m for _ in range(n)]
    
    # cnt[0][0] = 1
    stack = deque()
    stack.append((0,0,1))
    
    while stack:
        i, j, cnt = stack.popleft()
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni< n and 0<=nj<m and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                if ni == n-1 and nj == m-1:
                    answer = cnt + 1
                    check = 1
                    break
                
                stack.append((ni, nj, cnt+1))
                # cnt[ni][nj] = cnt[i][j] + 1
        if check == 1:
            
            break
            # if cnt[n-1][m-1] != n*m + 1:
            #     break

    
    # for i in range(n):
    #     for j in range(m):
    #         print(cnt[i][j],end='')
    #     print()

    # for i in range(n):
    #     for j in range(m):
    #         print(visited[i][j],end='')
    #     print()

    # if visited[n-1][m-1] == 1:
    #     answer = cnt[n-1][m-1]

    return answer



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))