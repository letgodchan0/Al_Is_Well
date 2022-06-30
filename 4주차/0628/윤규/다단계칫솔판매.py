## index 메소드 쓰는 순간 시간 너무 오래걸림 
def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0] * n
    
    persondict = dict()
    per = dict()
        
    for i in range(n-1, -1, -1):
        if referral[i] != '-' :
            persondict[enroll[i]] = (i, referral[i])
    for i in range(n):
        per[enroll[i]] = i

    for i in range(len(seller)):
        person = seller[i]
        # 판매금이 있고
        money = amount[i] * 100
        j = per[person]
        if money  < 10:
            answer[j] += money
            continue
        # 추천인이 있다면
        while persondict.get(person):
            # 돈의 10프로가 1이 넘는다면
            res = persondict[person]
            if money >= 10:
                answer[res[0]] += (money - int(0.1*money))
                person = res[1]
                money = int(0.1*money)
                
            else:
                answer[res[0]] += money
                money = 0
                break

        j = per[person]
        if money >= 10:
            answer[j] += money - int(0.1*money)
        else:
            answer[j] += money
   
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]



print(solution(enroll, referral, seller, amount))