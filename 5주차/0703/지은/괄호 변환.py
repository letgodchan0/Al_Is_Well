def check(u):
    stack = []
    for b in u:
        if b == '(':
            stack.append(b)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def divide(p):
    o, c = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            o += 1
        else:
            c += 1
        if o == c:
            return p[:i + 1], p[i + 1:]

def solution(p):
    if not p:
        return ''

    u, v = divide(p)

    if check(u):
        return u+solution(v)

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

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))