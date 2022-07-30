from collections import deque
import sys
def bfs(i, j):
    q = deque([])
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 1 and not visited[ni][nj]:
                visited[ni][nj] = 2
                q.append((ni, nj))


def f(n, start, length):
    global data
    if length == 3:
        tmp = []
        for i in range(len(check)):
            if check[i] == 1:
                tmp.append(result[i])
        data.append(tmp)
    elif n == start:
        return
    else:
        check[start] = 1
        f(n, start+1, length + 1)
        check[start] = 0
        f(n, start+1, length)


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [] # 0인 좌표 담기
lst = []  # 2인 좌표 담기
data = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            result.append((i, j))
        if arr[i][j] == 2:
            lst.append((i, j))

check = [0] * len(result) # 부분집합 만들기
f(len(result), 0, 0)  # 좌표 3개 부분집합 생성
answer = [] # 안전영역 개수 담아주기
for num in data:
    for tmp in num:     # 0 3개를 1로 바꿔주기
        i, j = tmp[0], tmp[1]
        arr[i][j] = 1
    visited = [[0] * m for _ in range(n)]
    for i, j in lst:
        bfs(i, j)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not arr[i][j] and not visited[i][j] :
                cnt += 1
    answer.append(cnt)
    for tmp in num:
        i, j = tmp[0], tmp[1]
        arr[i][j] = 0
print(max(answer))