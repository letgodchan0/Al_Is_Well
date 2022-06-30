def solution(brown, yellow):
    tmp=[]
    # yellow의 약수의 곱읍 구해서 tmp에 담아준다.
    for i in range(1,yellow+1):
        if yellow%i==0:
            divisor=sorted([yellow//i,i])
            if divisor in tmp:
                break
            tmp.append(divisor)
    answer=[]
    for i in tmp:
        if sum(i)==(brown-4)//2:
            answer.extend(i)
    result=[]
    result.append(answer[1]+2)
    result.append((brown+yellow)//result[0])
    return result