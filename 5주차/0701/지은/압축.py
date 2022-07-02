def solution(msg):
    answer = []

    di = {}
    for key, value in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)):
        di[key] = value

    i, j = 0, 0
    while True:
        j+=1
        if j == len(msg):
            answer.append(di[msg[i:]])
            return answer
        if msg[i:j+1] not in di:
            di[msg[i:j+1]] = len(di) + 1
            answer.append(di[msg[i:j]])
            i = j

print(solution('KAKAO'))