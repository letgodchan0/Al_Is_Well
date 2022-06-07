def solution(s):

    string = []

    for i in s:
        if len(string) > 0 and string[-1] == i:
            string.pop()
        else:
            string.append(i)

    if string:
        return 0
    else:
        return 1