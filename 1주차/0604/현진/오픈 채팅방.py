# 오픈채팅방
def solution(record):
    answer = []
    name = {}
    
    for i in record:
        i_split = i.split()
        if len(i_split) == 3:
            name[i_split[1]] = i_split[2]
    
    for j in record:
        j_split = j.split()
        if j_split[0] == 'Enter':
            answer.append(f'{name[j_split[1]]}님이 들어왔습니다.')
        elif j_split[0] == 'Leave':
            answer.append(f'{name[j_split[1]]}님이 나갔습니다.')
            
    return answer