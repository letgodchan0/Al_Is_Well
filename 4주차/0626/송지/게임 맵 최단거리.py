def solution(maps):
    
    v = [[0] * len(maps[0]) for _ in range(len(maps))]
    v[0][0] = 1
    now = [[0, 0]]
    can = 0
    answer = 1
    
    while now:
        new_now = []
        answer += 1
        for (i, j) in now:
            for (di, dj) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and maps[ni][nj] and not v[ni][nj]:
                    v[ni][nj] = 1
                    new_now.append([ni, nj])
                    if ni == len(maps) - 1 and nj == len(maps[0]) - 1:
                        can = 1
        now = new_now
        if can:
            break
    
    if not can:
        answer = -1
        
    return answer