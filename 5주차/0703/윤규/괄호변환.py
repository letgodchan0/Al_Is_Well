

def divide(w):
    check1 = 0
    check2 = 0
    for i in range(len(w)):
        if w[i] == "(":
            check1 += 1
        elif w[i] == ")":
            check2 += 1
        if check1 == check2:
            u = w[:i+1]
            v = w[i+1:]
            break
    return u, v

def right(w):
    check1 = 0
    check2 = 0
    for i in range(len(w)):
        if w[i] == "(":
            check1 += 1
        elif w[i] == ")":
            check2 += 1
        if check1 < check2:
            return 0
    return 1



def solution(p):
    answer = ''
    if p == '':
        return ''
    else:
        u, v = divide(p)
        if right(u):
            return u + solution(v)
        if not right(u):
            u = u[1:-1]
            newu = ''
            for i in range(len(u)):
                if u[i] == '(':
                    newu += ')'
                elif u[i] == ')':
                    newu += '('
            return "(" + solution(v) + ")" + newu
        
    return answer


print(solution("()))((()"))