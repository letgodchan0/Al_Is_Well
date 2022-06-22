def solution(n, t, m, p):   
    #진법, 미리 구할 숫자의 갯수, 게임에 참가하는 인원, 튜브의 순서
    answer = ''
    a = 0
    cnvrt = '0'
    chng = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while len(cnvrt) <= t * m:
        a += 1
        num = a
        temp = ''
        while (num):
            num, mo = divmod(num, n)
            if mo>=10:
                temp += chng[mo]   
            else:
                temp += str(mo)
        cnvrt += temp[::-1]

    for i in range(len(cnvrt)):
        if i % m == p-1:
            answer += str(cnvrt[i])
    return answer[:t]