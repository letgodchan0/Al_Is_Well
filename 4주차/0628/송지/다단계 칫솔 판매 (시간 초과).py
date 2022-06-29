import math

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    
    for i in range(len(seller)):
        now = amount[i] * 100
        person = seller[i]
        
        while now:
            num = enroll.index(person)
            gain = math.ceil(now * 0.9)
            answer[num] += gain
            now -= gain
            if referral[num] == '-':
                now = 0
            else:
                person = referral[num]
        
    return answer