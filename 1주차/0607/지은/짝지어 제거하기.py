def solution(s):
    word = []

    for a in s:
        if not word or word[-1]!=a:
            word.append(a)
        elif word[-1]==a:
            word.pop()

    answer = 0 if word else 1

    return answer
