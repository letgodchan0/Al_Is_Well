def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total + 1):
        if (total / i) % 1 == 0:
            j = total / i
            if j >= i:
                if 2 * j + 2 * i == brown + 4:
                    return [j, i]
    return answer  