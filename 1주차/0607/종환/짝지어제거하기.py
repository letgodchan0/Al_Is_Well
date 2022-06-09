"""
처음부터 차례로 스택에 넣는 방식
들어오는 값이 스택 맨 윗 값과 같다면, 스택 맨 윗 값을 pop, 다르다면 push
스택에 값이 남아있으면 0, 없으면 1
"""



def solution(s):
    # answer = -1
    stack = []

    for i in s:
        if len(stack) and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack):
        answer = 0
    else:
        answer = 1

    return answer