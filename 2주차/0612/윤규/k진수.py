
def solution(n, k):
    
    # k진법으로 변환
    if k == 10:
        k_n = str(n)
    else:
        k_n = ''
        while n >= k:
            k_n = str(n%k) + k_n
            n = n//k
            if n < k :
                k_n = str(n) + k_n
    # 0기준 나누기  
    numbers = list(map(str, k_n.split('0')))
    
    # 소수 찾기
    # 소수 판별 할때 전부 다 하면 시간 초과 난다....
    # 제곱근까지만 
    cnt = 0
    for number in numbers:
        if number != '':
            number = int(number)
            if number == 2:
                cnt += 1
            elif number > 2:
                for i in range(2, int(number**(1/2)+1)):
                    if number % i == 0:
                        break
                else:
                    cnt += 1
 
    return cnt