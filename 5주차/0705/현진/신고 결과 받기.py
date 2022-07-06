def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    lst = {}
    check = {}

    for i in report:
        a, b = i.split(' ')
        if b not in check:
            check[b] = 1
        else:
            check[b] += 1
        
        if a not in lst:
            lst[a] = [b]
        else:
            if b not in lst[b]:
                lst[a] += [b]
    
    for i, j in check.items():
        if j >= k:
            for user, user2 in lst.items():
                if i in user2:
                    answer[id_list.index(user)] += 1
    return answer