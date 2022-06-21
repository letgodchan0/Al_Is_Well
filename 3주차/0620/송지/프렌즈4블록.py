def solution(m, n, board2):
    answer = 0
    
    for i in range(m):
        board2[i] = list(board2[i])
        
    board = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            board[i][j] = board2[m - j - 1][i]
    
    print(board)
    
    while True:
        lst = []
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    lst.append([i, j])
                    
        if not lst:
            break
        
        for (i, j) in lst:
            board[i][j] = board[i + 1][j] = board[i][j + 1] = board[i + 1][j + 1] = 0
            
        for i in range(n):
            cnt = 0
            for j in range(m):
                if not board[i][j]:
                    cnt += 1
            if cnt == m:
                continue
            for k in range(cnt):
                board[i].remove(0)
                board[i] += [0]
        
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                answer += 1
    
    return answer