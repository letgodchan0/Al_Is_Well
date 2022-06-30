def hanoi(n, start, end, mid):
    if n==1:
        return [[start, end]]
    return hanoi(n-1, start, mid, end) + [[start, end]] + hanoi(n-1, mid, end, start)

def solution(n):
    return hanoi(n, 1, 3, 2)

