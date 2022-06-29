def hanoi(n, start, end, mid):
    global answer
    if n == 1:
        answer.append([start, end])
    else:
        hanoi(n - 1, start, mid, end)
        answer.append([start, end])
        hanoi(n - 1, mid, end, start)

def solution(n):

    global answer
    answer = []
    hanoi(n, 1, 3, 2)
    return answer