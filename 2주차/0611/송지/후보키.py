from itertools import combinations

def solution(relation):
    com = []
    for i in range(1, len(relation) + 1):
        com.extend(list(combinations(list(range(len(relation[0]))), i)))
        
    print(com)
    
    unique = []
    for comb in com:
        tmp = [tuple([info[i] for i in comb]) for info in relation]
        if len(set(tmp)) == len(relation):
            unique.append(comb)
            
    print(unique)
            
    answer = unique
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.remove(unique[j])
    
    return answer