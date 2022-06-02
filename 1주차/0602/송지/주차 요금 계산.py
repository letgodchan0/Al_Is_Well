import math
# 기본 시간(분) / 기본 요금(원) / 단위 시간(분) / 단위 요금(원)

def solution(fees, records):
    lst = []
    answer = []
    
    for record in records:
        a, b, c = record.split(' ')
        if c == 'IN':
            for car in lst:
                if car[0] == b:
                    car[2] = int(a[0:2]) * 60  + int(a[3:])
                    car[3] = 0
                    break
            else:
                lst.append([b, 0, int(a[0:2]) * 60  + int(a[3:]), 0])
        else:
            for car in lst:
                if car[0] == b:
                    car[1] += (int(a[0:2]) * 60  + int(a[3:]) - car[2])
                    car[3] = 1
                    break
            
    # 리스트 : [차 번호, 주차 시간, 마지막 입차 시간, 출차 여부]
    for car in lst:
        if car[3] == 0:
            car[1] += (23 * 60 + 59 - car[2])
    
    lst.sort()
    
    for car in lst:
        if car[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((car[1] - fees[0]) / fees[2]) * fees[3])
            
    return answer