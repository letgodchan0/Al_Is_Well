def solution(dartResult):
    answer = 0
    scores = []
    op = -1
    check = 0
    for i in range(len(dartResult)):
        if '0'<= dartResult[i] <='9':
            if check == 0:
                score = dartResult[i]
                op += 1
                check = 1
            else:
                score += dartResult[i]
        elif dartResult[i] == 'S' :
            check = 0
            scores.append(int(score))
        elif dartResult[i] == 'D' :
            check = 0
            scores.append(int(score) ** 2)
        elif dartResult[i] == 'T' :
            check = 0
            scores.append(int(score) ** 3)
        elif dartResult[i] == '*':
            check = 0
            if op == 0:
                scores[op] *= 2
            else:
                scores[op-1] *= 2
                scores[op] *= 2
        elif dartResult[i] == '#':
            check = 0
            scores[op] *= -1
        

    answer = sum(scores)
    return answer

dartResult = "1D2S#10S"
print(solution(dartResult))
