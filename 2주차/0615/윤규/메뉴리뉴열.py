from itertools import combinations

def solution(orders, course):
    answer = []
    
    # dic 은 가능한 메뉴 조합
    dic = {}
    pos = {}
    # key 는 원하는 조합 갯수, value 는 조합
    for num in course:
        pos[num] = [0,0]

    for order in orders:        # for 문 안에서는 sorted(order) 사용 불가능
        order = sorted(order)
        for num in course:
            for comb in tuple(combinations(order, num)):
    
                dic[comb] = 0
            
    for order in orders:
        order = sorted(order)
        for num in course:
            for comb in tuple(combinations(order, num)):
                dic[comb] += 1
    print(dic)
    # key 는 가능한 조합 , value는 갯수
    for key, value in dic.items():
        if value >=2 and value > pos[len(key)][1]:
            pos[len(key)] = [key, value]
        elif value >=2 and value == pos[len(key)][1]:
            pos[len(key)].extend([key, value])
    
    for value in pos.values():
        for val in value:
            if type(val) == tuple:
                menu = ''
                for v in val:
                    menu += v
                answer.append(menu)
    answer.sort()
    return answer




orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))