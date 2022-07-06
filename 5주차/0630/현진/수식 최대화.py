# 코딩테스트 연습 > 2020 카카오 인턴쉽 > 수식 최대화
from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    operations = ['*', '+', '-']

    stack = []
    tmp = 0
    for i, j in enumerate(expression):
        if j in ['*', '+', '-']:
            stack.append(expression[tmp:i])
            stack.append(j)
            tmp = i + 1
    else:
        stack.append(expression[tmp:])
    #expression에 없는 연산자는 operations에서 제거
    for operation in operations:
        if operation not in operations:
            operations.remove(operation)
    # operations에 있는 연산자로 구성할 수 있는 모든 우선순위 생성
    primarity = permutations(operations)

    for case in primarity:
        stacks = [deque(stack), deque()]
        temp = 1
        for c in case:
            temp = (temp + 1) % 2
            temp2 = (temp + 1) % 2
            while len(stacks[temp]):
                item = stacks[temp].popleft()
                if len(stacks[temp2]) and stacks[temp2][-1] == c:
                    c = stacks[temp2].pop()
                    n = stacks[temp2].pop()
                    item = str(eval(str(n) + c + str(item)))
                stacks[temp2].append(item)

        result = stacks[len(operations) % 2].pop()
        result = abs(int(result))
        answer = max(answer, result)
        
    return answer