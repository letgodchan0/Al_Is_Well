from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    #메뉴별 가능한 모든 음식 조합 만들기
    for n in course:    #n: 메뉴의 개수
        candidates = []
        for menu_lst in orders:
            for menu in combinations(menu_lst, n):
                candidates.append(''.join(sorted(menu)))

        sorted_candidates = Counter(candidates).most_common()
        #Counter(a): a에서 요소들의 개수를 세어, 딕셔너리 형태로 반환
        #.most_common(): 개수가 많은 순으로 정렬된 튜플 배열 리스트를 리턴한다
        
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))