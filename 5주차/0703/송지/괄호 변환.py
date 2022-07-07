def solution(p):
    answer = ''
    if not p: return answer
    
    cnt = 0
    start = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            
        if cnt == 0:
            u = p[start : i + 1]
            v = ''
            if i - 1 < len(p):
                v = p[i + 1:]
            if u[0] == '(':
                u = p[start:i + 1]
                answer += u
                answer += solution(v)
                return answer
            else:
                answer += '('
                answer += solution(v)
                answer += ')'
                for j in range(1, len(u) - 1):
                    if u[j] == '(':
                        answer += ')'
                    else:
                        answer += '('
                return answer
            
    return answer