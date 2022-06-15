from itertools import combinations
from collections import Counter
from unittest.util import sorted_list_difference

def solution(orders, course):
    answer = []
    for i in course:
        candidates = []
        for menu_lst in orders:
            for lst in combinations(menu_lst, i):
                result = ''.join(sorted(lst))
                candidates.append(result)
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)