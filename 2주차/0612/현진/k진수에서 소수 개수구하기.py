def solution(n, k):
    word = ''
    while n:
        word = str(n % k) + word
        n = n // k
    
    word = word.split('0')

    cnt = 0
    for w in word:
        if len(w) == 0:
            continue
        if int(w) < 2:
            continue
        prime = True
        for i in range(2, int(int(w) ** 0.5) + 1):
            if int(w) % i == 0:
                prime = False
                break
        if prime:
            cnt += 1
    return cnt