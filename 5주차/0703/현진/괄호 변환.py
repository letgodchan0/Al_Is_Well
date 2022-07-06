# 문자열 p를 u, v로 분리하는 함수
def divide(p):
    open_p = 0
    close_p = 0

    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i + 1], p[i + 1]

# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def check(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if not p:
        return ''
    
    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
                
        return answer