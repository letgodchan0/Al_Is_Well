from itertools import combinations
# 유일성 확인
def unique (tmp):
    if len(tmp)==len(set(tmp)):
        return True
    else:
        return False

# 최소성 확인 해주는 함수
def minimum(result):
    tmp=[]
    for i in range(2, len(result)):
        tmp.extend(list(combinations(result,i)))
    
    if all(unique(list(zip(*i)))==False for i in tmp) and unique(list(zip(*result))):
        return True
    else:
        return False

def solution(relation):
    check=[]
    # 혼자 유일성을 가진 애들이 answer에 담김
    answer=[]
    for i in list(zip(*relation)):
        if unique(i):
            answer.append(i)
        else:
            check.append(i)
    # 혼자 유일성을 갖지 못하는 애들을 조합해서 comp에 담음
    comp=[]
    for i in range(2,len(check)+1):
        comp.extend(list(combinations(check,i)))
    # comp에 있는 애들 중 유일성을 만족하는 애들만 result에 저장
    result=[]
    for i in comp:
        if unique(list(zip(*i))):
            result.append(i)
    # result에 있는 애들 중 최소성을 만족하는 애들만 answer에 담음
    for i in result:
        if minimum(i):
            answer.append(i)
    return len(answer)