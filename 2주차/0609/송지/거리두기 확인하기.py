def solution(places):
    answer = []
    dt = ([1, 0], [0, 1], [-1, 0], [0, -1])
    
    for place in places:
        ans = 1
        
        for i in range(5):
            for j in range(5):
                
                if place[i][j] == 'P':
                    for (di, dj) in dt:
                        ni = di + i
                        nj = dj + j
                        if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                            ans = 0
                            break
                
                if place[i][j] == 'O':
                    p = 0
                    for (di, dj) in dt:
                        ni = di + i
                        nj = dj + j
                        if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                            p += 1
                            if p >= 2:
                                ans = 0
                                break
                                
                if not ans:
                    break
            if not ans:
                break
                
        answer.append(ans)
        
    return answer