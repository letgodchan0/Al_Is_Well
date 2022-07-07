def solution(msg):
    answer = []
    dic = {chr(i + 64): i for i in range(1, 27)}
    cnt = 27
    i = 0
    search = ''
    
    while i < len(msg):
        search += msg[i]
        if search in dic:
            i += 1
        else:
            dic[search] = cnt
            cnt += 1
            s = search[:-1]
            answer.append(dic[s])
            search = ''
    
    answer.append(dic[search])
    return answer