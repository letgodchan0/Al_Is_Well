from ast import operator
from itertools import permutations

def solution(expression):
    operators = ['*', '+', '-']
    answer = []

    for op in permutations(operators, 3):
        tmp = ['']
        for ex in expression:
            if ex.isdigit() and tmp[-1] not in operators:
                tmp[-1] += ex
            else:
                tmp.append(ex)
        for i in op:
            while i in tmp:
                idx = tmp.index(i)
                tmp = tmp[:idx - 1] + [str(eval(''.join(tmp[idx - 1: idx + 2])))] + tmp[idx + 2:]
        answer.append(abs(int(tmp[0])))
    return max(answer)