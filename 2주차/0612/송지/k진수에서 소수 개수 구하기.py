def solution(n, k):
    answer = 0
    
    num = ''
    while n >= k:
        num += str(n % k)
        n = n // k
    num += str(n)
    num = num[::-1]
    
    n = []
    lst = []
    
    for i in range(len(num)):
        if num[i] != '0':
            n.append(num[i])
        elif num[i] == '0' and n:
            lst.append(int(''.join(n)))
            n = []
    
    if n:
        lst.append(int(''.join(n)))
        
    print(lst)
    
    for number in lst:
        if number != 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    break
            else:
                answer += 1
        
    return answer