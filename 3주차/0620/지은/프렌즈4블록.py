arr = []
def check(m, n, board):
    global arr
    arr = []
    for x in range(m):
            for y in range(n):
                if x in range(m-1) and y in range(n-1):
                    if board[x][y] == board[x+1][y]==board[x][y+1]==board[x+1][y+1] and board[x][y]!='':
                        arr.append((x,y))
    return arr

def rotate(b):
    return [list(elem) for elem in zip(*b[::-1])]

def solution(m, n, board):  #판 높이, 폭, 배치정보
    global arr
    answer = 0  #지워질 블록
    for i in range(m):
        board.append(list(board[i]))
    board = board[m:]

    while check(m, n, board) != []:
        while arr:
            x, y = arr.pop()
            board[x][y] = ''
            board[x+1][y] = ''
            board[x][y+1] = ''
            board[x+1][y+1] = ''

        board = rotate(board)

        for p in range(n):
            while '' in board[p]:
                board[p].remove('')
            for _ in range(m - len(board[p])):
                board[p].append('')

        board = rotate(board)
        board = rotate(board)
        board = rotate(board)       

    for p in range(m):
        answer += board[p].count('')

    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	))
