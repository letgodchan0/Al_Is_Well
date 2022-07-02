def solution(str1, str2):
    one = []
    two = []
    n_set = []  #교집합
    u_set = []  #합집합
    str1 = str1.upper()
    str2 = str2.upper()

    for i in range(0,len(str1)-1):
        if str1[i:i+2].isalpha():
            one.append(str1[i:i+2])
    for j in range(0,len(str2)-1):
        if str2[j:j+2].isalpha():
            two.append(str2[j:j+2])
    
    #교집합
    tmp_two = two[:]
    for o in one:   
        if o in tmp_two:
            n_set.append(o)
            tmp_two.remove(o)

    #합집합
    u_set = one[:]
    tmp_n = n_set[:]
    for t in two:
        if t not in tmp_n:
            u_set.append(t)
        else:
            tmp_n.remove(t)
    print(n_set)
    if len(n_set)==0 and len(u_set)==0: #두 집합이 모두 공집합일 경우
        return 65536

    return len(n_set)*65536//len(u_set) 

print(solution('di di mi mi mi mi', 'di di di go'))