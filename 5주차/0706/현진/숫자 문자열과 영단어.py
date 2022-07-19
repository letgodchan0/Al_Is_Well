def solution(s):
    answer = 0
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in number:
        s = s.replace(i, str(number.index(i)))
    return int(s)