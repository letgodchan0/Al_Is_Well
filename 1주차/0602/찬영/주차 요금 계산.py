import math
def solution(fees, records):
    basic_minute = fees[0]
    basic_fee = fees[1]
    minute = fees[2]
    unit = fees[3]

    car = list(set(map(lambda x: x.split()[1], records)))
    total_fees = {k : 0 for k in car}
    check = {}
    for record in records:
        tmp = record.split(' ')
        if tmp[1] not in check.keys():
            check[tmp[1]]= tmp[0]
        else:
            if tmp[-1] == 'OUT':
                out_time = int(tmp[0].split(':')[0]) * 60 + int(tmp[0].split(':')[1])
                in_time = int(check[tmp[1]].split(':')[0]) * 60 + int(check[tmp[1]].split(':')[1])
                total_fees[tmp[1]] = total_fees[tmp[1]] + out_time - in_time
                del check[tmp[1]]

    if check:
        for i in check.keys():
            out_time = 1439
            in_time = int(check[i].split(':')[0]) * 60 + int(check[i].split(':')[1])
            total_fees[i] = total_fees[i] + out_time - in_time

    result = []
    for i in total_fees.items():
        if i[1] <= basic_minute :
            result.append((i[0], basic_fee))
        else:
            result.append((i[0], basic_fee + (math.ceil((i[1] - basic_minute) / minute) * unit)))

    return list(map(lambda x: x[1], sorted(result)))