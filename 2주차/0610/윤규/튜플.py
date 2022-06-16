def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.replace(',', ' ')
   
    lst = list(map(int, s.split(' ')))
    
    dic = {}
    for i in range(len(lst)):
        if dic.get(lst[i]) == None:
            dic[lst[i]] = 1
        else:
            dic[lst[i]] += 1
    lst2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(len(lst2)):
        answer.append(lst2[i][0])
    
    return answer





s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
solution(s)
