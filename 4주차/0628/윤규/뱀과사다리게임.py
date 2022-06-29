


n, m = map(int, input().split(' '))
ladder = dict()
snake = dict()
for _ in range(n):
    s, e = map(int, input().split(' '))
    ladder[s] = e
for _ in range(m):
    s, e = map(int, input().split(' '))
    snake[s] = e


minV = 17

def search(i, cnt):
    global minV
    if i in visited and cnt > visited[i]:
        return
    if i > 100:
        return
    if cnt >= minV:
        return
    if i == 100:
        if minV > cnt:
            minV = cnt
        return
    
    for j in range(1, 7):
        k = i + j
        if k in ladder:
            k = ladder[k]
        elif k in snake:
            k = snake[k]
        visited[k] = cnt+1
        search(k, cnt+1)
        
        
visited = dict()
visited[1] = 0
search(1, 0)
print(minV)
