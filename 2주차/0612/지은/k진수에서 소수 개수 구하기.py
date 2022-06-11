def is_prime(nu):   #소수 판별
    if nu==1:
        return False
    for i in range(2, int(nu**0.5)+1):
        if nu%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    n_k = ''    #k진수로 변환한 n

    #정수 n을 k진수로 바꾼다
    while n:
        n, m = n//k, n%k
        n_k += str(m)
    n_k = n_k[::-1]
    
    nums = n_k.split('0')   #0을 기준으로 split

    for num in nums:
        if num=='':
            continue
        if is_prime(int(num)):
            answer += 1

    return answer