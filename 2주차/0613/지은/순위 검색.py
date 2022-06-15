# #시간 초과...
# def solution(info, query):
#     answer = []
#     splited_info = []
#     for nf in info:
#         nf = nf.split()
#         splited_info.append(nf)

#     for qry in query:
#         qry = qry.split()
#         candidates = splited_info[:]
#         rmv_lst = []    #전에 걸러진 인덱스들

#         for q in qry:
            
#             if q=='and' or q=='-':
#                 continue

#             for i in range(len(candidates)):
#                 if i in rmv_lst:
#                     continue
#                 if q.isdigit():
#                     if int(q) > int(candidates[i][-1]):
#                         rmv_lst.append(i)
#                 elif not q in candidates[i]:
#                     rmv_lst.append(i)

#         answer.append(len(candidates)-len(rmv_lst))

#     return answer

#최종 코드
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    data = {}
    #해쉬테이블 사용(파이썬에서는 딕셔너리 자료형으로 제공) key만 알고 있으면 바로 value에 접근 가능.
    #-를 고려한 모든 경우의 수를 만들어 key로 넣어둔다. 조건에 해당하는 점수들을 value로.

    for nf in info:
        tmp = nf.split()
        conditions = tmp[:-1]   #score 제외 조건
        score = int(tmp[-1])
        cond_keys = []
        
        for i in range(5):  #'-' 고려한 조건 만들기. 
            for combi in combinations(conditions, i):   #i(0~4)개 모은 조합
                cond_keys = ''.join(list(combi))
                data.setdefault(cond_keys,[]).append(score)
                #.setdefault(key[, default]): key가 딕셔너리에 있으면 value를 돌려준다
                #그렇지 않으면 default 값을 갖는 key를 삽입한 후 default를 돌려줌
                #여기에서는 data에서 cond_keys라는 key가 있으면 그 value를 돌려주고 아니라면 빈 리스트를 반환한 후 거기에 score를 append

    for key in data.keys():
        data[key].sort()    #value들 sort

    for qry in query:
        qry = qry.split()
        q = ''.join([s for s in qry[0:7] if s != "-" and s !="and"]) #-와 and를 제외하고 score 뺀 조건들 뭉친다
        score = int(qry[-1])
        if q not in data.keys():    
            answer.append(0)
        else:
            result = data[q]
            idx = bisect_left(result, score)  #이진탐색으로 원하는 값 이상이 처음 나오는 위치 찾는다
            #bisect_left: score가 이미 있는 값이라면 기존 항목의 앞 위치를 반환
            answer.append(len(result) - idx)
    
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])