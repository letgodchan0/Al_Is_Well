from itertools import permutations

def calc(expression, p):
    for i in range(len(expression)):
        expression[i] = expression[i].split(p[1])
    n = []
    for i in range(len(expression)):
        temp = []
        for e in range(len(expression[i])):
            if p[0] in expression[i][e]:
                temp.append(str(eval(expression[i][e])))
                continue
            temp.append(expression[i][e])
        n.append(temp)

    expression = []
    for i in range(len(n)):
        if len(n[i]) > 1:
            expression.append(str(eval(p[1].join(n[i]))))
            continue
        expression.append(n[i][0])
    return abs(eval(p[-1].join(expression)))

def solution(expression):
    answer = 0
    for p in permutations("+-*", 3):
        n = expression.split(p[-1])
        answer = max(answer, calc(n, p))
    return answer