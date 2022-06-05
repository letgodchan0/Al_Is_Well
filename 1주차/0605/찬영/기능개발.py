def solution(progresses, speeds):
    import math
    rest=[]
    answer=[]
    for i in range(len(progresses)):
        rest.append(math.ceil((100-progresses[i])/speeds[i]))
    while True:
        cnt=0
        if len(rest)==0:
            break
        
        for i in range(len(rest)):
            if rest[i]<= rest[0]:
                cnt+=1
            else:
                break
        answer.append(cnt)
        rest=rest[cnt:]

    return answer