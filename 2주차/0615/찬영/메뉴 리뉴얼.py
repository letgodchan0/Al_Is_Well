from itertools import combinations
from collections import Counter
def solution(orders, course):
    result=[]
    for i in course:
        if i > len(max(orders, key = len)):
            break
        # i 수 만큼 음식 조합을 check에 담기
        check=[]
        for j in orders:
            j=sorted(j)
            check.extend(list(map(lambda x:''.join(x),(combinations(j,i)))))
        # Counter을 이용해서 조합별로 갯수 세기
        tmp=Counter(check)
        max_num=tmp.most_common(1)[0][1]
        # 가장 많이 선택된 조합 찾기
        print(tmp)
        for k in tmp:
            if tmp[k]==max_num and tmp[k]>1:
                result.append(k)

#     answer=[sorted(i) for i in list(map(list, result))]
    answer=list(map(''.join, [sorted(i) for i in list(map(list, result))]))
    answer=list(set(answer))
    sorted(answer)
    return sorted(list(set(answer)))