from collections import deque

def solution(maps):
    R = len(maps)
    C = len(maps[0])
    maze = [[-1 for _ in range(C)] for _ in range(R)]
    queue = deque()
    queue.append([0, 0])
    maze[0][0] = 1
    while queue:
        j, i = queue.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= nj < R and 0 <= ni < C and maps[nj][ni] == 1:
                if maze[nj][ni] == -1:
                    maze[nj][ni] = maze[j][i] + 1
                    queue.append([nj, ni])
    answer = maze[-1][-1]
    return answer
