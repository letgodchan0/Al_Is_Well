def solution(n, t, m, p):
    answer = ''
    
    arr = []
    for i in range(t):
        arr.append(p + m * i - 1)
    print(arr)
    
    order = '0'
    num = 1
    while len(order) <= arr[-1]:
        s = num
        tmp = ''
        while s:
            if (s % n) >= 10:
                tmp += chr(55 + s % n)
            else:
                tmp += str(s % n)
            s = s // n
        order += tmp[::-1]
        num += 1
        
    for i in arr:
        answer += order[i]

    return answer