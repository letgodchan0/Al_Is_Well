def solution(record):
    name=[]
    action=[]
    answer = []
    key = {}
    result=[]
    
    for i in record:
        if i.split()[0]=='Enter':
            name.append(i.split()[1])
            action.append('님이 들어왔습니다.')
            key[i.split()[1]]=i.split()[2]
        if i.split()[0]=='Leave':
            name.append(i.split()[1])
            action.append('님이 나갔습니다.')
        if i.split()[0]=='Change':
            key[i.split()[1]]=i.split()[2]
    
    for i in name:
        i=key[i]
        answer.append(i)
    
    for i in range(len(answer)):
        result.append(answer[i]+action[i])
        
   
    return result