def solution(dartResult):
    score=['0','1','2','3','4','5','6','7','8','9','10']
    bonus=['S','D','T']
    result=[]
    dartResult = dartResult.replace('10','k')
    dartResult=['10' if i=='k' else i for i in dartResult]
    for i in range(len(dartResult)):
        answer=0
        if dartResult[i] in score:
            if dartResult[i+1] =='S':
                answer=int(dartResult[i])**1
            if dartResult[i+1] =='D':
                answer=int(dartResult[i])**2
            if dartResult[i+1] =='T':
                answer=int(dartResult[i])**3
            result.append(answer)
        elif dartResult[i] =='*':
            if len(result)==1:
                result[0]=result[0]*2
            else:
                result[-1]=result[-1]*2
                result[-2]=result[-2]*2
        elif dartResult[i] =='#':
            result[-1]=-result[-1]
        else:
            continue
    return sum(result)