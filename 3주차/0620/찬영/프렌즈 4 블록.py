def find(m,n,board):
    tmp=[]
    cnt=0 # 팡팡의 갯수를 세주기 위해서    
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j]!=board[i][j+1]:
                continue
            else:
                if board[i+1][j]==board[i][j] and board[i+1][j+1]==board[i][j] and board[i][j]!='팡팡':
                    tmp.append([i,j])
    for i in tmp:
        a=i[0]
        b=i[1]
        board[a][b]='팡팡'
        board[a+1][b]='팡팡'
        board[a][b+1]='팡팡'
        board[a+1][b+1]='팡팡'
    
    board=list(zip(*board))
    board=list(map(list, board))
    new_board=[]
    for i in board:
        new_board.append(sorted(i, key=lambda x: -len(x)))
    new_board=list(zip(*new_board))
    new_board=list(map(list, new_board))
    
    return new_board

def solution(m, n, board):
    board=list(map(list, board))
    answer=find(m,n,board)
    if answer!=board:
        while True:
            if answer==find(m,n,answer):
                break
            else:
                answer=find(m,n,answer)
    cnt=0
    for i in answer:
        for j in i:
            if j=='팡팡':
                cnt+=1
    return cnt