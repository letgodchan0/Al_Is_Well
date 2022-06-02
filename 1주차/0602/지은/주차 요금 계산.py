import math
def solution(fees, records):
    answer = []
    cars_fees = []    #차와 요금
    new_records={}
    for record in records:  #키는 차 번호, in, out 순으로 시간 저장
        if record[6:10] in new_records:
            new_records[record[6:10]].append(record[:5])
        else:   
            new_records[record[6:10]] = [record[:5]]
    for new_record in new_records:
        car = new_record
        times = new_records[car]
        pay_m = 0   #누적 주차시간
        if len(times)%2:    #저장된 시간이 홀수개라면(마지막 출차정보 없음)
            times.append('23:59')
        for i in range(len(times)//2):
            m = int(times[2*i+1][3:]) - int(times[2*i][3:])
            h = int(times[2*i+1][:2]) - int(times[2*i][:2])
            pay_m += (h * 60 + m)   
        if pay_m < fees[0]: #기본 시간보다 적게 주차했을 경우
            fee = fees[1]   
        else:
            fee = fees[1] + math.ceil((pay_m - fees[0])/fees[2]) * fees[3]
        cars_fees.append([car, fee])
    cars_fees.sort()
    for car_fee in cars_fees:
        answer.append(car_fee[1])
    return answer