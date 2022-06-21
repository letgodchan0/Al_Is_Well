d = [(0, 1), (1, 0), (1, 1)]
def solution(m, n, board):
    
    answer = 0
    glst = []
    
    for i in range(m):
        row = []
        for ch in board[i]:
            row.append(ch)
        glst.append(row)

    def sb():
        block = set()
        for i in range(m):
            for j in range(n):
                if glst[i][j] != '0':
                    c = glst[i][j]
                    for di, dj in d:
                        ni, nj = i + di, j + dj
                        if 0<=ni<m and 0<=nj<n:
                            if glst[ni][nj] != c:
                                break
                        else:
                            break
                    else:
                        block.add((i,j))
                        block.add((i+1,j+1))
                        block.add((i+1,j))
                        block.add((i,j+1))
        for i,j in block:
            glst[i][j] = '0'
        return len(block)
    #내려가는 코드
    def down():
        for j in range(n):
            chars = []
            check = 0
            check2 = 0
            for i in range(m-1,-1,-1):
                
                if glst[i][j] == '0':
                    check = 1
                elif glst[i][j] != '0':
                    chars.append(glst[i][j])
                    if check == 1:
                        check2 = 1

            
            if check2 == 1:
                for i in range(m-1,-1,-1):
                    if chars:
                        glst[i][j] = chars.pop(0)
                    else:
                        glst[i][j] = '0'

            


    # for i in range(m):
    #     for j in range(n):
    #         print(glst[i][j], end='')
    #     print()

    # print('ㅡㅡㅡㅡㅡㅡㅡㅡ')

    # cnt = sb()
    # print(cnt)
    
    # for i in range(m):
    #     for j in range(n):
    #         print(glst[i][j], end='')
    #     print()

    # print('ㅡㅡㅡㅡㅡㅡㅡㅡ')

    # down()

    # for i in range(m):
    #     for j in range(n):
    #         print(glst[i][j], end='')
    #     print()

    # print('ㅡㅡㅡㅡㅡㅡㅡㅡ')

    # cnt = sb()
    # print(cnt)

    # for i in range(m):
    #     for j in range(n):
    #         print(glst[i][j], end='')
    #     print()

    # print('ㅡㅡㅡㅡㅡㅡㅡㅡ')


    cnt = sb()

    while cnt != 0:
        answer += cnt
        down()
        cnt = sb()
    return answer




board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
m, n = 6, 6
print(solution(m,n,board))


# a = set()
# print(len(a))