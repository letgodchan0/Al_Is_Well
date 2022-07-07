def solution(s):
    answer = 0
    eng = ['zero', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine']
    for idx, i in enumerate(eng):
        s = s.replace(i, str(idx))
    return int(s)
print(solution("one4seveneight"))
