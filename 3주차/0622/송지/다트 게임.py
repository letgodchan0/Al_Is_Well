def solution(dartResult):
    
    dartResult = dartResult.replace('10', '^')
    
    cat1 = cat2 = 0    
    for i in range(2, len(dartResult)):
        if (dartResult[i].isdigit() or dartResult[i] == '^') and not cat1:
            cat1 = i
        elif dartResult[i].isdigit() or dartResult[i] == '^':
            cat2 = i
            break
            
    result = [dartResult[:cat1], dartResult[cat1:cat2], dartResult[cat2:]]
    answer = [0, 0, 0]
    
    for i in range(3):
        
        if result[i][0].isdigit():
            answer[i] = int(result[i][0])
        else:
            answer[i] = 10
        
        if result[i][1] == 'D':
            answer[i] **= 2
        elif result[i][1] == 'T':
            answer[i] **= 3
        
        if len(result[i]) == 3:
            if result[i][2] == '*':
                try:
                    answer[i] *= 2
                    answer[i - 1] *= 2
                except:
                    pass
            else:
                answer[i] *= -1
    
    return sum(answer)