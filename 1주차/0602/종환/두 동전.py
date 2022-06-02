"""
풀이 과정
N, M이 1이상 20이하이다.
버튼으로 동전을 상, 하, 좌, 우로 움직일 수 있는데, 
10번을 초과하여 움직여도 한 개의 동전만을 떨어뜨릴 수 없으면 -1을 출력한다.
(-1 <= print <= 10) 재귀?
- 조건
1. 동전이 두 개 모두 남아있으면 계속해서 움직여야 함.
2. 동전이 두 개 모두 떨어졌다면 해당 결과는 폐기해야 함.
3. 동전이 하나만 남았다면 (하나만 떨어졌다면) 종료해야 함. (결과값 비교+대입)
4. 10번의 움직임이 끝났다면 해당 움직임은 끝내야 함.

--------- 21시 30분 추가
두 동전 중 하나만 떨어져도 끝날 수 있는 BFS를 사용하자.
BFS + 백트래킹 사용


"""
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

N, M = map(int,input().split())

board = []

visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]   # 4차원
## 'o' - 동전, '.' - 빈 칸  , '#' - 벽
for i in range(N):
    data = list(input())
    board.append(data)

# 동전 좌표 저장
coin_pos = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coin_pos.append((i,j))


def bfs():
    q = deque()
    q.append((coin_pos[0][0], coin_pos[0][1], coin_pos[1][0], coin_pos[1][1],0))
    
    visited[coin_pos[0][0]][coin_pos[0][1]][coin_pos[1][0]][coin_pos[1][1]] = 1
    
    while q:
        pos = q.popleft()
        if pos[4] >= 10:
            return -1
        for i in range(4):
            #동전 1
            next_y_1 = pos[0] + dy[i]
            next_x_1 = pos[1] + dx[i]
            #동전 2
            next_y_2 = pos[2] + dy[i]
            next_x_2 = pos[3] + dx[i]

            # 이동
            if 0 <= next_y_1 < N and 0 <= next_x_1 < M and 0 <= next_y_2 < N and 0 <= next_y_2 < N and 0 <= next_x_2 < M:
                if not visited[next_y_1][next_x_1][next_y_2][next_x_2]:
                    if board[next_y_1][next_x_1] == "#":
                        next_y_1, next_x_1 = pos[0], pos[1]
                    if board[next_y_2][next_x_2] == "#":
                        next_y_2, next_x_2 = pos[2], pos[3]
                    visited[next_y_1][next_x_1][next_y_2][next_x_2] = 1
                    q.append((next_y_1,next_x_1,next_y_2,next_x_2, pos[4]+1))
            
            # 결과 출력
            elif 0 <= next_y_2 < N and 0 <= next_y_2 < N and 0 <= next_x_2 < M: 
                return pos[4] + 1
            elif 0 <= next_y_1 < N and 0 <= next_x_1 < M:
                return pos[4] + 1


print(bfs())