def solution(id_list, report, k):
    repdic = dict()
    id_dic = dict()
    answer = [0] * len(id_list)
    for index, name in enumerate(id_list):
        id_dic[name] = index
    for i in range(len(report)):
        p1, p2 = report[i].split(' ')
        if repdic.get(p2):
            repdic[p2].add(p1)
        else:
            repdic[p2] = {p1}

    for key, value in repdic.items():
        if len(value) >= k:
            for name in value:
                answer[id_dic[name]] += 1

    return answer



id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))