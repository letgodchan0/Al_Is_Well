import sys

def bfs(x, y):
    q = set([])
    q.add((x, y, arr[x][y], 1))
    answer = 0
    while q:
        x, y, word, cnt = q.pop()
        if cnt > answer:
            answer = cnt
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in word:
                q.add((nx, ny, word+arr[nx][ny], cnt+1))

    return answer
r, c = map(int, input().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
print(bfs(0,0))