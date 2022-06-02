from collections import deque

def bfs(coin1, coin2):
    x, y = coin1; xx, yy = coin2
    q = deque([])
    q.append((x, y, xx, yy, 0))
    while q:
        x, y, xx, yy, cnt = q.popleft()
        if cnt > 10:
            return -1

        if arr[x][y] == 0 or arr[xx][yy] == 0:
            if arr[x][y] == 0 and arr[xx][yy] == 0:
                pass
            else:
                return cnt

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny, nxx, nyy = x + dx, y + dy, xx + dx, yy + dy
            # 동전이 하나라도 떨어지는 경우
            if arr[nx][ny] == 0 or arr[nxx][nyy] == 0:
                if arr[nx][ny] == 0 and arr[nxx][nyy] != 0:
                    if cnt < 10:
                        return cnt + 1
                    else:
                        return -1
                elif arr[nx][ny] != 0 and arr[nxx][nyy] == 0:
                    if cnt < 10:
                        return cnt + 1
                    else:
                        return -1
            else:
                if arr[nx][ny] != '#' and arr[nxx][nyy] != '#':
                    q.append((nx, ny, nxx, nyy, cnt+1))
                elif arr[nx][ny] != '#' and arr[nxx][nyy] == '#':
                    q.append((nx, ny, xx, yy, cnt+1))
                elif arr[nx][ny] == '#' and arr[nxx][nyy] != '#':
                    q.append((x, y, nxx, nyy, cnt+1))
    return -1
n, m = map(int, input().split())
arr = [[0] * (m+2)] + [[0] + list(input()) + [0] for _ in range(n)] + [[0] * (m+2)]
coin = []
for i in range(n+1):
    for j in range(m+1):
        if arr[i][j] == 'o':
            coin.append([i, j])
    if len(coin) == 2:
        break
coin1, coin2 = coin
print(bfs(coin1, coin2))