def solution(name):
    answer = 0

    def dif(a, b):
        if a == b:
            return 0
        elif a < b:
            return min(ord(b) - ord(a), 26 + ord(a) - ord(b))
        else:
            return min(ord(a) - ord(b), 26 + ord(b) - ord(a))
    cnt = []
    z = 0
    for alpha in name:
        a = dif(alpha, 'A')
        cnt.append(a)
        if a == 0:
            z += 1
    cnt2 = cnt[:]
    k = len(cnt) - z
    answer = sum(cnt) 
    minV = len(name)-1


    def counting(i, j, c, cnt):
        nonlocal minV
        if c > minV:
            return

        if len(cnt)*(-1) > i or i >= len(cnt):
            return

        v = cnt[i]
        check = 0
        if v != 0:
            cnt[i] = -1
            check = 1

        cnt2 = cnt[:]
        
        if sum(cnt) == k*(-1):
            if minV > c:
                minV = c
            return


        
        counting(i+j, j, c+1, cnt)
        
        

        if len(cnt)*(-1) <= i+j < len(cnt) and cnt[i+j] == 0:
            counting(i-j,-1*j, c+1, cnt2)
        if check == 1:
            cnt[i] = v

    
    counting(0, 1, 0, cnt)
    cnt = cnt2[:]
    counting(0, -1, 0, cnt)


    answer += minV
    # for i in range(1, len(name)):
    #     if cnt[0 + i] == 0:
    #         checkr += 1
    #     else:
    #         break
    # for i in range(1, len(name)):
    #     if cnt[0 - i] == 0:
    #         checkl += 1
    #     else:
    #         break
    # answer -= max(checkr, checkl)
        
    
    return answer



print(solution("JAN"))