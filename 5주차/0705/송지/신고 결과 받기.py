def solution(id_list, report, k):
    declare_list = [set() for _ in range(len(id_list))] 
    count = [0] * len(id_list)
    answer = [0] * len(id_list)
    
    for rep in report:
        a, b = rep.split(' ')
        temp = len(declare_list[id_list.index(a)])
        declare_list[id_list.index(a)].add(b)
        
        if temp != len(declare_list[id_list.index(a)]):
            count[id_list.index(b)] += 1
    warn_list = []
    
    for i in range(len(id_list)):
        if count[i] >= k:
            warn_list.append(id_list[i])
    
    for i in range(len(declare_list)):
        for d in declare_list[i]:
            if d in warn_list:
                answer[i] += 1
        
    return answer