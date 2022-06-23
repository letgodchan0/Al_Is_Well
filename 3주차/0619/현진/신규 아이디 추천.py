def solution(new_id):
    new_id = new_id.lower()
    answer = ''

    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    answer = 'a' if answer == '' else answer

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))
    return answer