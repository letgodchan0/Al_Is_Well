def switch(i, n):
    dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    base = ''
    if i < n:
        if i >= 10:
            base = dic[i]
        else:
            base = str(i)
    while i >= n:
        # 몫, 나머지
        i, mod = divmod(i, n)
        if mod >= 10:
            mod = dic[mod]
        base = str(mod) + base
        if i < n:
            if i >= 10:
                ni = dic[i]
                base = ni + base
            else:
                base = str(i) + base
    return base



def solution(n, t, m, p):
    
    answer = ''
    numbers = t * m
    pos = ''
    for i in range(numbers):
        pos += switch(i, n)
   
    for i in range(p-1, len(pos), m):
        answer += pos[i]
        if len(answer) == t:
            break

    return answer


print(solution(16,16,2,1))

a,b = divmod(28,16)
print(type(a), type(b))
print(a, b)