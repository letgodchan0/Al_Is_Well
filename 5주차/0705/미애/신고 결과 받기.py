from collections import defaultdict
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    answer = []
    #print(list(set(report)))
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)

    for i in report:
        a, b = i.split()
        user[a].add(b)
        cnt[b] += 1

    for j in id_list:
        result = 0
        for l in user[j]:
            if cnt[l] >= k:
                result += 1
        answer.append(result)
    return answer

solution(id_list, report, k)