
def solution(brown, yellow):
    answer = []
    cnt = brown + yellow
    for row in range(int(cnt**(1/2)), cnt):
        if cnt % row == 0:
            answer = [row, cnt//row]
            if cnt//row > row:
                answer = [cnt//row, row]
            if (answer[0]-2)*(answer[1]-2) == yellow:
                break
    return answer