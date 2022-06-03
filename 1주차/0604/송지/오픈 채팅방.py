def solution(record):
    answer = []
    now = {}
    
    for r in record:
        lst = list(r.split(' '))
        
        if lst[0] == 'Change' or lst[0] == 'Enter':
            now[lst[1]] = lst[2]
            
    # print(now)
    
    for r in record:
        lst = list(r.split(' '))
        
        if lst[0] == 'Enter':
            answer.append(f'{now[lst[1]]}님이 들어왔습니다.')
        elif lst[0] == 'Leave':
            answer.append(f'{now[lst[1]]}님이 나갔습니다.')
    
    return answer