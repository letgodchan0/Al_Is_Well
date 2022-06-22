def change(number,base):
    s = "0123456789ABCDEF"
    q,r = divmod(number,base)
    n = s[r]
    return change(q, base) + n if q else n


def solution(n, t, m, p):
    answer = []
    lst = []
    for i in range(0,t*m,1):
        lst.append(change(i,n))
    text = "".join(lst)
    i = 0
    while(len(answer) < t):
        answer.append(text[i:i + m][p - 1])
        i = i + m
    return "".join(answer)