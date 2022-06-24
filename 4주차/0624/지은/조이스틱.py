def solution(name):
    answer = float('inf')  #조이스틱 조작횟수

    if set(name)=={'A'}:   #name에 A만 들어있을 때
        return 0

    for i in range(len(name) // 2): #좌우로 조작 / 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:   #['i에서 좌로만 움직임', 'i에서 우로만 움직임']
            while n and n[-1] == 'A':   #맨 마지막이 'A'라면 'A' 제외해버리기
                n = n[:-1]
            row_move = i + len(n) - 1   
            answer = min(answer, row_move)

    for j in range(len(name)):  #상하로 조작
        answer += min(ord(name[j]) - ord('A'),  26 + ord('A') - ord(name[j]))

    return answer 
print(solution('ANBAN'))