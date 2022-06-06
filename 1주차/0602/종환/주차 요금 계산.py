"""
주차요금
총 이용 분수 기준으로
180분 이하: 5000원
180분 초과: 초과 분에 한하여 10분마다 600원 (한자리수 분 단위는 올림 계산)
fees: 주차 요금을 나타내는 정수 배열 (0: 기본 시간(분), 1: 기본 요금(원), 2: 단위 시간(분), 3: 단위 요금(원))
records: 입/출차 내역을 나타내는 문자열 배열 "시각 차량번호 내역" (ex. "00:59 5382 IN", "05:23 5382 OUT")
(출차하지 않았을 경우, 23:59에 출차한 것으로 간주)

조건
1. 차량번호가 작은 자동차부터
2. 청구할 주차 요금을 차례대로 정수 배열(ex.answer)에 담아서 return
"""
# 필요한 것: records에서 차량번호를 받았을 때, 차량 번호가 없다면, 추가할 딕셔너리?
#     {
#         "5382": 여기서 00:59를 00*60+59=59를 저장해야 함 (이용시간(분) 만큼)
#     }
#         차량이 주차 중인지, 나갔는지 확인할 딕셔너리 (모두 끝났을 때, 이 딕셔너리 차량 중 "IN" 상태인 차량이 있으면 23:59에서 뺌)
#     {
#         "5382": "IN",
#         "0000": "OUT",
#     }
# 딕셔너리를 키 값 (차량번호) 순으로 정렬 (새 딕셔너리 이름 = sorted(딕셔너리이름.items()))
# 새 딕셔너리에서 값을 하나씩 리스트에 넣기 (for key, value in 새 딕셔너리 이름.items():  새 리스트.append(value))
import math

# fees = [180, 5000, 10, 600]
# records = [
#     "34:49 4545 IN"
# ]

def solution(fees, records):
    # 주차시간
    parked_time = {}
    # 주차여부
    parked_now = {}

    # 한 줄씩 해석해서 주차시간 구하기
    for line in records:
        tmp = list(str, line.split())
        
        # 처음 들어오는 차인 경우
        if tmp[2] == "IN" and tmp[1] not in parked_now:
            parked_now[tmp[1]] = "IN"
            parked_time[tmp[1]] = - (int(tmp[0][0:2]) * 60 + int(tmp[0][3:]))
        # 나가는 차인 경우
        elif tmp[2] == "OUT":
            parked_now[tmp[1]] = "OUT"
            parked_time[tmp[1]] = parked_time[tmp[1]] + (int(tmp[0][0:2]) * 60 + int(tmp[0][3:]))
        # 두번째로 들어오는 차인 경우
        elif tmp[2] == "IN" and tmp[1] in parked_now:
            parked_now[tmp[1]] = "IN"
            parked_time[tmp[1]] = parked_time[tmp[1]] - (int(tmp[0][0:2]) * 60 + int(tmp[0][3:]))

    # OUT 기록이 없는 경우 계산
    for line in parked_now:
        if line == "OUT":
            parked_time[line] = parked_time[line] + (23*60+59)

    # 주차요금 계산
    for key, value in parked_time:
        if value >= fees[0]:
            value = fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3]
        else:
            value = fees[1]

    # 주차요금 출력
    result_dict = sorted(parked_time.items())
    answer = []
    for fee in result_dict:
        answer.append(fee[1])
    return answer

