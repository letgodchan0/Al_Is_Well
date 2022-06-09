"""
시계방향 회전
위-> 왼쪽 -> 아래 -> 오른쪽 순서로 밀 것
오른쪽 위 값을 저장해두고, 나중에 넣어준다. ( tmp )

"""
def solution(rows, columns, queries):

    answer = []
    arr = [[0] * columns for _ in range(rows)]
    t = 1
    for y in range(rows):
        for x in range(columns):
            arr[y][x] = t
            t += 1
    
    
    for y1, x1, y2, x2 in queries:
        tmp = arr[y1-1][x1-1]
        min_rectangle = tmp

        for i in range(y1 - 1, y2 - 1):
            mov = arr[i+1][x1-1]
            arr[i][x1-1] = mov
            min_rectangle = min(min_rectangle, mov)
        
        for i in range(x1 - 1, x2 - 1):
            mov = arr[y2-1][i+1]
            arr[y2-1][i] = mov
            min_rectangle = min(min_rectangle, mov)
        
        for i in range(y2 - 1, y1 - 1, -1): # 반대
            mov = arr[i-1][x2-1]
            arr[i][x2-1] = mov
            min_rectangle = min(min_rectangle, mov)
        
        for i in range(x2 - 1, x1 - 1, -1): # 반대
            mov = arr[y1-1][i-1]
            arr[y1-1][i] = mov
            min_rectangle = min(min_rectangle, mov)
        
        arr[y1-1][x1] = tmp
        answer.append(min_rectangle)
    
    return answer