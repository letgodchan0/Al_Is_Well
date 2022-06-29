# 코딩테스트 연습 > 탐욕법(Greedy) > 구명보트
def solution(people, limit):
    # people 정렬
    people.sort()
    cnt = 0
    # 인덱스로 people 리스트 접근
    first = 0   # 가장 가벼운 사람
    last = len(people) - 1  # 가장 무거운 사람
    while first <= last:
        cnt += 1
        # 가장 가벼운 사람과 가장 작은 사람의 값을 더해서 limit 값과 비교
        if people[last] + people[first] <= limit:
            first += 1
        last -= 1
    return cnt