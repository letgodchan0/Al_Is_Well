def solution(dr):
    lst = [0,0,0]
    idx = -1
    #점수(0-10)보너스(S,D,T)옵션(*,#)
    for i in range(len(dr)):
        if dr[i]=='0' and dr[i-1]=='1' and i >=1:
            continue
        elif (dr[i]=='1' and dr[i+1]=='0' and i<len(dr)-1) or dr[i].isdigit():
            idx += 1
            if dr[i]=='1' and dr[i+1]=='0':
                lst[idx] = 10
            else: 
                lst[idx] = int(dr[i])
        elif dr[i] in ['S','D', 'T']:
            if dr[i] == 'S':
                pass
            elif dr[i] == 'D':
                lst[idx]**=2
            elif dr[i] == 'T':
                lst[idx]**=3
        else:
            if dr[i] == '*':
                lst[idx] *= 2
                lst[idx-1] *= 2
            elif dr[i] == '#':
                lst[idx] *= -1
    return sum(lst)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))