def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = i * columns + j + 1
            
    for queri in queries:
        min_num = 10000
        
        i = queri[0] - 1
        j = queri[1] - 1
        prev = arr[i][j]
        
        while j != queri[3] - 1:
            if arr[i][j] < min_num:
                min_num = arr[i][j]
            temp = arr[i][j]
            arr[i][j] = prev
            prev = temp
            j += 1
            
        while i != queri[2] - 1:
            if arr[i][j] < min_num:
                min_num = arr[i][j]
            temp = arr[i][j]
            arr[i][j] = prev
            prev = temp
            i += 1
            
        while j != queri[1] - 1:
            if arr[i][j] < min_num:
                min_num = arr[i][j]
            temp = arr[i][j]
            arr[i][j] = prev
            prev = temp
            j -= 1
            
        while i != queri[0] - 1:
            if arr[i][j] < min_num:
                min_num = arr[i][j]
            temp = arr[i][j]
            arr[i][j] = prev
            prev = temp
            i -= 1
            
        arr[i][j] = prev
        if prev < min_num:
            min_num = prev
            
        answer.append(min_num)
        
    
    return answer