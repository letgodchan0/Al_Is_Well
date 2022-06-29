# def find(parents, money, number, answer):
#     if parents[number] == number or money // 10 == 0:
#         answer[number] += money
#         return
#     send = money // 10
#     mine = money - send
#     answer[number] += mine
#     find(answer, send, parents[number], answer)
#     return

# def solution(enroll, referral, seller, amount):
#     n = len(enroll) # 총 사람 수(민호 제외)
#     answer = [0] * (n + 1)  # 민호 포함
#     dictionary = {} # 이름-번호의 key-value를 가지는 딕셔너리
#     parents = [i for i in range(n + 1)] # 각자 자신을 부모로 초기화
#     # 이름-번호로 딕셔너리에 저장
#     for i in range(n):
#         dictionary[enroll[i]] = i + 1
#     # 추천인 입력
#     for i in range(n):
#         if referral[i] == '-':
#             parents[i + 1] = 0
#         else:
#             parents[i + 1] = dictionary[referral[i]]
#     # 칫솔정산
#     for i in range(len(seller)):
#         find(parents, amount[i] * 100, dictionary[seller[i]], answer)
#     return answer[1:]
import math

def solution(enroll, referral, seller, amount):
    parentTree = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0 for i in range(len(enroll))]))

    for i in range(len(seller)):
        earn = amount[i] * 100
        target = seller[i]

        while True:
            # 10원 단위 이하라면 모두 받고 레퍼럴
            if earn < 10:
                answer[target] += earn
                break
            else:
                answer[target] += math.ceil(earn * 0.9)
                if parentTree[target] == '-':
                    break
                earn = math.floor(earn * 0.1)
                target = parentTree[target]
    return list(answer.values())