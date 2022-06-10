def solution(s):
    answer=''
    result=[]
    empty=[]
    for i in s[1:-1]:
        if i.isdigit():
            answer+=i
        else:
            if answer.isdigit():
                empty.append(int(answer))
                answer=''
            if i=='}':
                result.append(list(empty))
                empty=[]
    result=sorted(result, key=lambda x:len(x))[::-1]

    good=[]
    for i in range(len(result)):
        if i==len(result)-1:
            good.append(result[i][0])
        else:
            good.append(list(set(result[i])-set(result[i+1]))[0])
    return good[::-1]