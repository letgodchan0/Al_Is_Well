def perfect(p):
    s = []
    for i in p:
        if i == '(':
            s.append(i)
        else:
            if not s:
                return False
            s.pop()
    return True

def new(p):
    left, right = 0, 0
    u = ''
    v = ''
    for idx, i in enumerate(p):
        if i == '(':
           left += 1
        else:
            right += 1
        if left == right:
            return p[:idx+1], p[idx+1:] #u, v



# 올바른 괄호 문자열
def solution(p):
    if not p:
        return ""

    u, v = new(p)
    if perfect(u):
        return u + solution(v)
    else:
        # u가 올바르지 않은 문자열 - 바꿔워야해
        answer = '('
        answer += solution(v)
        answer += ')'
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer

p = "()))((()"
print(solution(p))