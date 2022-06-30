def solution(people, limit):
    people.sort()
    answer=0
    start=0
    end=len(people)-1
    while start < end:
        if people[start]+people[end] > limit:
            end-=1
        else:
            start+=1
            end-=1
        answer+=1
        
        if start==end:
            answer+=1
    return answer