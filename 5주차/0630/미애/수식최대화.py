# 2. 계산할 것
def calc(exp, op):
    global result
    # 피연산자 연산자 구분
    arr = []
    temp = ""
    for a in exp:
        # 아스키코드가 숫자인 경우
        if ord(a) >= 48:
            temp += a
        else:
            arr.append(int(temp))
            arr.append(a)
            temp = ""
    arr.append(int(temp))

    # 연산자따라 계산 - 스택이용
    for o in op:
        stack = []
        while len(arr) != 0:
            i = arr.pop(0)
            # print(o, i, stack, arr)
            if i == o:
                # 연산자라면 계산하기
                if o == '+':
                    stack.append(stack.pop() + arr.pop(0))
                if o == '-':
                    stack.append(stack.pop() - arr.pop(0))
                if o == '*':
                    stack.append(stack.pop() * arr.pop(0))
            else:
                # 피연산자라면 stack에 넣기
                stack.append(i)
        arr = stack
        # print(len(stack))
        if len(stack) == 1:
            return abs(stack[0])

# 1. 연산자 우선순위
from itertools import permutations

def solution(expression):
    global result
    op_lst = ['*', '+', '-']
    ops = list(permutations(op_lst, 3))
    result = []
    for op in ops:
        result.append(calc(expression, op))
    answer = max(result)
    return answer

print(solution("50*6-3*2"))
