def solution(pro, speeds):
    ans = []
    goal = len(pro)
    
    while sum(ans) < goal:
        for i in range(len(pro)):
            pro[i] += speeds[i]
        
        if pro[0] >= 100:
            l = 1
            for i in range(1, len(pro)):
                if pro[i] >= 100:
                    l += 1
                else:
                    break
            pro = pro[i:]
            speeds = speeds[i:]
            ans.append(l)
    
    return ans