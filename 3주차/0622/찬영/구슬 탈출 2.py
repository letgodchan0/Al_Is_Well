from collections import deque
import copy
import sys

def bfs(r1, r2, b1, b2, arr):
    cnt = 0
    q = deque([])
    q.append((r1, r2, b1, b2, cnt, arr))
    visited = [(r1, r2, b1, b2)]
    while q:
        r1, r2, b1, b2, cnt, arr = q.popleft()
        if arr[r1][r2] == 'O' and cnt <= 10:
            return cnt
        elif cnt == 10:
            return -1

        if cnt > 10:
            return -1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # 아래 while문이 벽을 만나서 종료된 경우 True, 파란공이 구멍을 만나면 False
            goal_red = False
            goal_blue = False
            check_red = False
            check_blue = False
            tmp = copy.deepcopy(arr)
            nr1, nr2 = r1, r2
            nb1, nb2 = b1, b2
            while True:
                if not check_red:
                    nr1, nr2 = nr1 + dx, nr2 + dy
                if not check_blue:
                    nb1, nb2 = nb1 + dx, nb2 + dy

                # 파란 구슬 이동 가능하면 옮기기
                if not check_blue:
                    if tmp[nb1][nb2] == '.':
                        tmp[nb1][nb2] = 'B'
                        tmp[nb1 - dx][nb2 - dy] = '.'

                    # 파란 구슬 자리가 벽또는 빨간 구슬 만나면 위치 고정
                    elif tmp[nb1][nb2] == '#':
                        nb1, nb2 = nb1 - dx, nb2 - dy
                        check_blue = True

                    elif tmp[nb1][nb2] == 'R':
                        # 파란 구슬 빨간 구슬이 붙어 있는경우, 빨간 구슬이 그 다음에 움직일 여지가 있음
                        if tmp[nb1 + dx][nb2 + dy] == '#':
                            check_blue = True
                        nb1, nb2 = nb1 - dx, nb2 - dy

                    elif tmp[nb1][nb2] == 'O':
                        goal_blue = True
                        break

                # 빨간 구슬이 더 이상 움직이지 못할 때 까지 움직이기
                if not check_red:
                    # 빨간 구슬 이동 가능하면 이동
                    if tmp[nr1][nr2] == '.':
                        tmp[nr1][nr2] = 'R'
                        tmp[nr1 - dx][nr2 - dy] = '.'

                    # 빨간 구슬 구멍 만남
                    elif tmp[nr1][nr2] == 'O':
                        tmp[nr1 - dx][nr2 - dy] = '.'  # 빨간 구슬 통과
                        goal_red = True
                        check_red = True

                    # 벽이나 파란 구슬 만나면 더 못가니까 break
                    elif tmp[nr1][nr2] == '#' or tmp[nr1][nr2] == 'B':
                        nr1, nr2 = nr1 - dx, nr2 - dy
                        check_red = True

                # 둘다 더 이상 못 움직이면,
                if check_red and check_blue:
                    break

            # 빨간 공 통과 파란공 통과 x
            if goal_red and not goal_blue:
                return cnt + 1

            # 파란 구슬이 구멍을 만나지 않은 경우
            if not goal_blue and (nr1, nr2, nb1, nb2) not in visited:
                q.append((nr1, nr2, nb1, nb2, cnt + 1, tmp))
                visited.append((nr1, nr2, nb1, nb2))
    return -1


n, m = map(int, input().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            r1, r2 = i, j
        elif arr[i][j] == 'B':
            b1, b2 = i, j

print(bfs(r1, r2, b1, b2, arr))