def solution(ss):
    answer = []
    num_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 
                'four':'4', 'five':'5', 'six':'6', 
                'seven':'7', 'eight':'8', 'nine':'9'}
    tmp = ''

    for s in ss:
        if tmp in num_dic:
            answer.append(num_dic[tmp])
            tmp = ''
        if s.isdigit():
            answer.append(str(s))
        else:
            tmp += s
    if tmp in num_dic:
        answer.append(num_dic[tmp])
    return int(''.join(answer))

print(solution("one4seveneight"))

