from itertools import combinations
from collections import defaultdict

def lower_bound(begin, end, target_list, target):
    if begin >= end:
        return begin
    mid = (begin + end) // 2
    if target_list[mid] >= target:
        return lower_bound(begin, mid, target_list, target)
    else:
        return lower_bound(mid+1, end, target_list, target)

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                dic[key].append(score)
    for value in dic.values():
        value.sort()
    
    for query in queries:
        query = query.replace('and ', '')
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        cnt = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = lower_bound(0, len(target_list), target_list, target_score)
            cnt = len(target_list) - idx
        answer.append(cnt)
    return answer