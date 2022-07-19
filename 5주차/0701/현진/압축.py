# 프로그래머스 > 2018 카카오 블라인드 채용 > 압축
def solution(msg):
    answer = []
    tmp = {chr(i + 64): i for i in range(1, 27)}
    num = 27

    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer