def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        compact = ''
        check = s[:i]
        cnt = 1

        for j in range(i, len(s), i):
            if check == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    compact = compact + str(cnt) + check
                else:
                    compact = compact + check
                check = s[j:j+i]
                cnt = 1
        if cnt != 1:
            compact = compact + str(cnt) + check
        else:
            compact = compact + check
        answer.append(len(compact))
    return min(answer)