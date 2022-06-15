def solution(info, query):
    
    answer = []
    
    for que in query:
        lst = list(que.split(' '))
        print(lst)
        
        ans = 0
        
        for pro in info:
            lst2 = list(pro.split(' '))
            for i in range(4):
                if lst[i * 2] != '-' and lst[i * 2] != lst2[i]:
                    break
            else:
                if int(lst2[4]) >= int(lst[-1]):
                    ans += 1
        
        answer.append(ans)
        
    return answer