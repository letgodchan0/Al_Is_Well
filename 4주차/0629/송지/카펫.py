def solution(brown, yellow):
    answer = []
    y = [1]
    tmp = yellow
    
    if yellow != 1:
        i = 1
        while yellow != 1:
            for i in range(2, yellow + 1):
                if yellow % i == 0:
                    break
            y.append(i)
            yellow = yellow // i

    print(y)
    yellow = tmp

    if len(y) <= 2:
        answer.append(max(y) + 2)
        answer.append(min(y) + 2)
    else:
        for i in range(2, brown, 2):
            print(i // 2, ((brown - i) // 2 - 2))
            if (i // 2) * ((brown - i) // 2 - 2) == yellow:
                answer.append((brown - i) // 2)
                answer.append(i // 2 + 2)
                break
    
    return answer