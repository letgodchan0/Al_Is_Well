def solution(name):
    answer = 0
    move = len(name) - 1
    next = 0
    
    while name[move] == 'A' and move > 0:
        move -= 1
    
    if (move < 0):
        return answer
        
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        move = min(move, i + (i + len(name)) - next)
    answer += move
    return answer