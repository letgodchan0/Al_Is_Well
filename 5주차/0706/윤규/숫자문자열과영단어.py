
word_dict = {"zero":"0", "one": "1" ,"two": "2" ,"three": "3" ,"four": "4" ,"five": "5" ,"six": "6" ,"seven": "7" ,"eight": "8" ,"nine": "9"}

def solution(s):
    answer = ''
    word = ''
    for a in s:
        if "0" <= a<='9':
            answer += a
        else:
            word += a
            if word_dict.get(word):
                answer += word_dict[word]
                word = ''

    answer = int(answer)
    return answer




print(solution("one4seveneight"))