from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    #전체 조합 구하기
    candidates = []
    for i in range(1, col+1):
        candidates.extend(combinations(range(col), i))  #extend는 iterable의 모든 항목을 넣는다
        
    #유일성 만족하는 경우만 거르기
    unique = []
    for candidate in candidates:
        tmp = [tuple([item[i] for i in candidate]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(candidate)

    #최소성 만족하지 않는 경우 제거
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])   #discard는 지우려는 element가 없어도 정상종료함 / remove는 없으면 KeyError

    return len(answer)