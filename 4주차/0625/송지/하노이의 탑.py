def solution(n):
    answer = []
    
    def hanoi(start, target, inter, n):
        if n == 1:
            answer.append([start, target])
        else:
            hanoi(start, inter, target, n - 1)
            hanoi(start, target, inter, 1)
            hanoi(inter, target, start, n - 1)
            
    hanoi(1, 3, 2, n)
    
    return answer