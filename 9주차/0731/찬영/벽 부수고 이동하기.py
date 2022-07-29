from collections import deque
def bfs():
    # q = [0] * (n*m*2)
    # front = -1
    # rear = 0
    # q[rear] = (0,0,0)
    # visited[0][0][0] = 1
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        i, j, check = q.popleft()
        if i == n-1 and j == m-1:
            return visited[i][j][check]

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
             # 벽이 아직 안뚤렸을 때
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj][check] == 0 and arr[ni][nj] == 0:
                visited[ni][nj][check] = visited[i][j][check] + 1
                q.append([ni, nj, check])
            # 벽 뚫을 때
            elif 0 <= ni < n and 0 <= nj < m and visited[ni][nj][check] == 0 and arr[ni][nj] == 1 and check == 0:
                visited[ni][nj][check+1] = visited[i][j][check] + 1
                q.append([ni, nj, check+1])
    return -1

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
visited= [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs())