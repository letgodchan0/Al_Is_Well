import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        target = queue.popleft()
        # 주사위 눈만큼 움직이기
        for i in range(1, 7):
            dice = target + i
            # 100칸이 넘어가면 continue
            if dice > 100:
                continue
            cnt = board[dice]
            # 탐색하지 않은 칸이라면 탐색한다.
            if visited[cnt] == 0:
                queue.append(cnt)
                visited[cnt] = visited[target] + 1
                # 100번째 칸까지 탐색완료하면 리턴
                if cnt == 100:
                    return

ladder, snake = map(int, input().split())
board = [i for i in range(101)]
for _ in range(ladder + snake):
    dice1, dice2 = map(int, input().split())
    board[dice1] = dice2

visited = [0] * 101
bfs(1)
print(visited[100] - 1)

