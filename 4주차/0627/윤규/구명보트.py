def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    i = 0
    j = len(people) - 1
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            j -= 1
        i += 1
        
    
    
    return answer






people = [70, 50, 80, 50, 30, 20]
limit = 100

print(solution(people, limit))