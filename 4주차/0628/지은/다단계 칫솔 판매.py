import math

def solution(enroll, referral, seller, amount):
    di = {}
    for i in range(len(enroll)):
        di[enroll[i]] = [referral[i], 0]

    for j in range(len(seller)):
        money = amount[j] * 100
        r = seller[j]

        while True:
            if money < 10:
                di[r][1] += money
                break
            else:
                di[r][1] += math.ceil(money * 0.9)
                if di[r][0] == '-':
                    break
                money = math.floor(money * 0.1)
                r = di[r][0]

    _, answer = zip(*(di.values()))
    return list(answer)

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))