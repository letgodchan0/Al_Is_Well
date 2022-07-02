def solution(id_list, report, k):
    di = {}
    mail = {}
    for key in id_list:
        di[key] = [0,[]]
        mail[key] = 0
    report = list(set(report))
    for rprt in report:
        u, s = rprt.split()
        di[s][0] += 1
        di[s][1].append(u)
    for d in di:
        if di[d][0]>=k:
            for n in di[d][1]:
                mail[n] += 1
    return list(mail.values())

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"],3))