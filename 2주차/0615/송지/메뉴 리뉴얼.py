from itertools import combinations

def solution(orders, course):
    
    arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    orders = sorted(orders, key = lambda x : len(x))
    dicts = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    
    for order in orders:
        menus = []
        for i in course:
            menus.append(list(combinations(list(order), i)))
        for menu in menus:
            for me in menu:
                so = sorted(list(me))
                name = ''.join(so)
                if name in dicts[len(name)]:
                    dicts[len(name)][name] += 1
                else:
                    dicts[len(name)][name] = 1
                    
    answer = []
    
    for i in course:
        max_value = 2
        max_key = []
        for (key, value) in dicts[i].items():
            if value > max_value:
                max_key = [key]
                max_value = value
            elif value == max_value:
                max_key.append(key)
        answer.extend(max_key)
    
    return sorted(answer)