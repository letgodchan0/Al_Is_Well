def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        now = -3
        lst = ['기본값']
        
        for j in range(len(s) // i):
            if lst[-1] == s[j * i:j * i + i]:
                if type(lst[-2]) == int:
                    lst[-2] += 1
                else:
                    lst.insert(-1, 2)
            else:
                lst.append(s[j * i:j * i + i])
        
        if len(s) % i:
            now += len(s) % i
        
        for c in lst:
            now += len(str(c))
            
        if now < answer:
            answer = now
                
        # print(lst, now - 3)
            
    return answer