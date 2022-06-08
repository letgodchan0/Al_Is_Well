# 행렬 테두리 회전하기
def solution(rows, columns, queries):
    answer = []
    table = []
    for i in range(rows):
        table.append([j for j in range(i * columns+1, (i + 1) * columns + 1)])
    
    for query in queries:
        query = [k-1 for k in query]
        tmp = table[query[0]][query[1]]
        minV = tmp

        # left
        for l in range(query[0] + 1, query[2] + 1):
            table[l - 1][query[1]] = table[l][query[1]]
            minV = min(minV, table[l][query[1]])
        # bottom
        for l in range(query[1] + 1, query[3] + 1):
            table[query[2]][l - 1] = table[query[2]][l]
            minV = min(minV, table[query[2]][l])
        # right
        for l in range(query[2] - 1, query[0] - 1, -1):
            table[l + 1][query[3]] = table[l][query[3]]
            minV = min(minV, table[l][query[3]])
        # top
        for l in range(query[3] - 1, query[1] - 1, - 1):
            table[query[0]][l + 1] = table[query[0]][l]
            minV = min(minV, table[query[0]][l])
        table[query[0]][query[1] + 1] = tmp
        answer.append(minV)

    return answer