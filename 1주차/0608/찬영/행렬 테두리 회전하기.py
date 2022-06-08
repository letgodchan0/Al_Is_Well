def solution(rows, columns, queries):
    arr = []
    for i in range(rows):
        arr.append(list(range(i * columns + 1, i * columns + columns + 1)))
    answer = []
    for query in queries:
        res = []
        x1, y1, x2, y2 = query
        x1 -= 1;
        y1 -= 1;
        x2 -= 1;
        y2 -= 1;

        # 처음 윗 줄
        tmp1 = arr[x1][y2]
        for i in range(y2, y1, -1):
            arr[x1][i] = arr[x1][i - 1]
            res.append(arr[x1][i])
        arr[x1][y1] = arr[x1 + 1][y1]
        res.append(arr[x1][y1])


        # 오른쪽
        tmp2 = arr[x2][y2]
        for i in range(x2, x1 + 1, -1):
            arr[i][y2] = arr[i - 1][y2]
            res.append(arr[i][y2])
        arr[x1 + 1][y2] = tmp1
        res.append(arr[x1 + 1][y2])

        # 아래
        tmp3 = arr[x2][y1]
        for i in range(y1, y2 - 1):
            arr[x2][i] = arr[x2][i + 1]
            res.append(arr[x2][i])
        arr[x2][y2 - 1] = tmp2
        res.append(arr[x2][y2 - 1])

        # 왼쪽
        for i in range(x1 + 1, x2 - 1):
            arr[i][y1] = arr[i + 1][y1]
            res.append(arr[i][y1])
        arr[x2 - 1][y1] = tmp3
        res.append(arr[x2 - 1][y1])

        answer.append(min(res))
    return answer
