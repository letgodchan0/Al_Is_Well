def solution(rows, columns, queries):
    answer = []
    arr = [[0]*(columns) for _ in range(rows)]
    
    n = 1
    for r in range(rows):  #행렬에 값을 넣어주는 과정
        for c in range(columns):
            arr[r][c]=n
            n+=1

    for query in queries:
        x1,y1,x2,y2 = query
        tmp = arr[x1-1][y1-1] #회전할 때 다른 값으로 대체되어지기 때문에
        mini = tmp  

        #구간을 나누어 이동
        for k in range(x1-1, x2-1):     #좌
            arr[k][y1-1] = arr[k+1][y1-1]
            mini = min(mini, arr[k][y1-1])

        for k in range(y1-1, y2-1):     #하
            arr[x2-1][k] = arr[x2-1][k+1]
            mini = min(mini, arr[x2-1][k])

        for k in range(x2-1, x1-1, -1): #우
            arr[k][y2-1] = arr[k-1][y2-1]
            mini = min(mini, arr[k][y2-1])

        for k in range(y2-1,y1-1,-1):   #상
            arr[x1-1][k] = arr[x1-1][k-1]
            mini = min(mini, arr[x1-1][k])

        arr[x1-1][y1] = tmp
        answer.append(mini)

    return answer