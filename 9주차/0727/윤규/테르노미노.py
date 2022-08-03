n, m = map(int, input().split(' '))
arr = [list(map(int, input().split(' '))) for _ in range(n)]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def tet(i, j):
    q = [(i, j, [(i, j)], arr[i][j])]
    res = []
    while q:
        x, y, visited, sum = q.pop()
        cnt = len(visited)
        if cnt == 4:
            res.append(sum)
        for di, dj in d:
            ni, nj = x + di, y + dj
            if cnt < 4:
                if 0<=ni<n and 0<=nj<m and (ni, nj) not in visited:
                    new_visited = visited + [(ni, nj)]
                    q.append((ni, nj, new_visited, sum + arr[ni][nj]))
                    
            
    return max(res)

def tet2(i, j):
    q = [(i, j, [(i, j)], arr[i][j])]
    res = []
    while q:
        x, y, visited, sum = q.pop()
        cnt = len(visited)
        if cnt == 4:
            res.append(sum)
        for di, dj in d:
            ni, nj = x + di, y + dj
            if cnt < 4:
                if cnt != 2:
                    if 0<=ni<n and 0<=nj<m and (ni, nj) not in visited:
                        new_visited = visited + [(ni, nj)]
                        q.append((ni, nj, new_visited, sum + arr[ni][nj]))
                        
                elif cnt == 2:
                    if 0<=ni<n and 0<=nj<m and (ni, nj) not in visited:
                        new_visited = visited + [(ni, nj)]
                        q.append((x, y, new_visited, sum + arr[ni][nj]))
    return max(res)

maxV = 0
for i in range(n):
    for j in range(m):
        if maxV < max(tet(i,j), tet2(i,j)):
            maxV = max(tet(i,j), tet2(i,j))


print(maxV)
