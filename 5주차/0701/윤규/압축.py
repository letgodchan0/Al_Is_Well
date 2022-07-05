def solution(msg):
    answer = []
    alpha = dict()
    for i in range(1, 27):
        alpha[chr(64+i)] = i
    word = ''
    num = 26
    i = 0
    while i < len(msg):
        b_word = word
        word += msg[i]
        if not alpha.get(word):
            answer.append(alpha[b_word])
            num += 1
            alpha[word] = num
            word = ''
            
        else:
            i += 1
    answer.append(alpha[word])
   
    return answer



msg = "KAKAO"
print(solution(msg))