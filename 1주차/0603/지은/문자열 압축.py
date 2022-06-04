def solution(s):
    words = []
    
    for x in range(1,len(s)//2+2): #x(1~문자열 절반) 단위로 문자열 자른다
        result = ''
        cnt = 1
        unit = s[:x] #단위 문자열
        for i in range(x, len(s)+x, x):
            if unit == s[i:i+x]: #슬라이싱한 것과 단위 문자열 같으면
                cnt += 1
            else:
                if cnt == 1:    #1을 생략하고 표현
                    result += unit
                else:
                    result += (str(cnt)+unit)
                unit = s[i:i+x] #표현 후 초기화
                cnt = 1
        words.append(result)
    answer = len(min(words, key = lambda x:len(x))) #words의 길이들 중 가장 짧은 것의 길이
    return answer
a = solution("a") 
print(a)

