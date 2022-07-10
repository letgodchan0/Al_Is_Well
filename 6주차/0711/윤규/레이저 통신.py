from collections import deque
import sys
input = sys.stdin.readline


w, h = map(int, input().split(' '))
t = max(w, h)
arr = [list(input()) for _ in range(h)]
visited = [[-1] * w for _ in range(h)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

check = 0 
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            c1i, c1j = i, j
            check = 1
            break
    if check == 1:
        break


q = deque()
q.append((c1i, c1j, 0))

visited[c1i][c1j] = 0
ck = 0
while q:
    i, j, cnt = q.popleft()
    if arr[i][j] == 'C' and (i != c1i or j != c1j):
        c2i, c2j = i, j
        break
    


    for di, dj in d:
        for k in range(1, t):
            ni, nj = i + di * k, j + dj * k
            # *이면 더이상못가게
            if 0<=ni<h and 0<=nj<w:
                if arr[ni][nj] == '*' :
                    break
                else:
                    if visited[ni][nj] == -1 or visited[ni][nj] > cnt:
                        q.append((ni, nj, cnt+1))
                        visited[ni][nj] = cnt 
            else:
                break

    # if ck == 2:
    #     for i in range(h):
    #         for j in range(w):
    #             print(visited[i][j], end=' ')
    #         print()
    # ck += 1
# print(visited)
print(visited[c2i][c2j] )