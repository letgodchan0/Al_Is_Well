from itertools import combinations_with_replacement

def solution(n, info):
    ans = 1
    answer = []
    
    arr = [i for i in range(11)]
    lst = list(combinations_with_replacement(arr, n))
    
    for com in lst:
        
        a = l = 0
        lion = [0] * 11
        for c in com:
            lion[c] += 1
        
        for i in range(10):
            if info[i] and info[i] >= lion[i]:
                a += 10 - i
            elif lion[i]:
                l += 10 - i
        
        if l - a > ans:
            answer = [lion]
            ans = l - a
        elif l - a >= ans:
            answer.append(lion)

    if not answer:
        return [-1]
    
    answer = sorted(answer, key = lambda x : (-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1]))
    
    return answer[0]